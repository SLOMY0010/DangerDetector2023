import tensorflow as tf
import cv2
import numpy as np
IMG_HEIGHT = 256
IMG_WIDTH = 256


def main():
    
    model = tf.keras.models.load_model(input('model path: '))

    img = scale_input(input('img: '))
    img = np.expand_dims(img/255, 0)

    yhat = model.predict(img)
    print(yhat)

    if yhat[0][0] > 0.5:
        print('NO')
    else:
        print('YES')

    print(yhat[0][0])


def scale_input(image):
    image = cv2.imread(image)
    print(image.shape)
    image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH))
    print(image.shape)
    return image


if __name__ == '__main__':
    main()