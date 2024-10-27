import tensorflow as tf
import os
import cv2
import imghdr
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

IMG_EXTS = ['jpeg', 'jpg', 'bmp', 'png']
NUM_CATEGORIES = 2
IMG_HEIGHT = 256
IMG_WIDTH = 256
TEST_SIZE = 0.1
EPOCHS = 8


def main():
    model_path = input("Name of model: example: 'models/fire_clf'\n")
    data_dir = input('Data Directory: ')
    clean_data(data_dir)

    images, labels = load_data(data_dir)
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    model = get_model()

    model.fit(x_train, y_train, epochs=EPOCHS)

    model.evaluate(x_test,  y_test, verbose=2)

    test = input("Do you wanna test the model? y or n\n")
    if test:
        img_path = input('image path: example: "test.jpg\n"')

        img = cv2.imread(img_path)
        img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH))
        img = np.expand_dims(img/255, 0)

        yhat = model.predict(img)

        print(yhat[0][0])
        if yhat[0][0] > 0.5:
            print("no")
        else:
            print('yep')

    # Save model to file
    save = input('do you wanna save the model? y or n\n')
    if 'y' in save:
        filename = model_path
        model.save(filename)
        print(f"Model saved to {filename}.")


def clean_data(data_dir):

    print('cleaning data...')
    for image_class in os.listdir(data_dir):
        for image in os.listdir(os.path.join(data_dir, image_class)):
            image_path = os.path.join(data_dir, image_class, image)
            try:
                img = cv2.imread(image_path)
                tip = imghdr.what(image_path)
                if tip not in IMG_EXTS:
                    print(f'issue with image{image_path}.\nit will be removed.')
                    os.remove(image_path)
            except Exception as e:
                os.remove(image_path)
                print(f'{image_path} removed.')
    print('Done cleaning.')


def load_data(data_dir):

    images_and_labels = (list(), list())
    for folder in range(NUM_CATEGORIES):
        images = os.listdir(os.path.join(data_dir, str(folder)))
        for image in images:
            image = cv2.imread(os.path.join(data_dir, str(folder), image))
            image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH))
            images_and_labels[0].append(image)
            images_and_labels[1].append(folder)

    return images_and_labels


def get_model():

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(
            16, (3,3), 1, activation='relu', input_shape=(256,256,3)
        ),
        
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Conv2D(
            32, (3,3), 1, activation='relu'
        ),
        
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Conv2D(
            16, (3,3), 1, activation='relu'
        ),

        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='sigmoid')

    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    
    return model


if __name__ == '__main__':
    main()

