import os
import tensorflow as tf
import cv2
import numpy as np

import send_warning


IMG_HEIGHT = 256
IMG_WIDTH = 256


def main():

    # Get the image
    img_path = input('image path: ')
    
    # Scale the image
    img = cv2.imread(img_path)
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH))
    img = np.expand_dims(img/255, 0)

    # Examine the image
    fire = is_fire(img)
    gun = is_gun(img)

    dangers = list()

    if fire:
        dangers.append('Fire')
        print("There is fire.")
    
    if gun:
        dangers.append('Gun')
        print("There is a gun.")

    if len(dangers) != 0:
        send_warning.send_mail(img_path, dangers)

    print(dangers)
    

def is_fire(img):
    model = tf.keras.models.load_model(os.path.join('models', 'fire_clf'))
    yhat = model.predict(img)
    
    return False if yhat[0][0] > 0.5 else True
            

def is_gun(img):
    model = tf.keras.models.load_model(os.path.join('models', 'gun_clf'))
    yhat = model.predict(img)
    
    return False if yhat[0][0] > 0.5 else True


if __name__ == '__main__':
    main()