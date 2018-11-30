# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro, for
# his workshop in PythonDay Mexico 2018 at CUCEA in Gdl, Mx.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

from keras.models import model_from_json
import numpy as np
import base64
import cv2


def net_loader(base_url):
    """
    Utility function to load a trained neural network.
    """

    # Load json and create model:
    json_file = open(base_url + 'model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # Load weights into loaded model:
    loaded_model.load_weights(base_url + "model.h5")
    print("Loaded model from disk")
    loaded_model.compile(loss='categorical_crossentropy',
                         optimizer='adam', metrics=['accuracy'])

    # Make prediction function:
    loaded_model._make_predict_function()

    return loaded_model


def base64_to_png(img_base64):
    """
    Utility function to convert from base64 to png.
    """
    imgdata = base64.b64decode(img_base64)
    with open('../assets/temp.png', 'wb') as f:
        f.write(imgdata)
    return


if __name__ == '__main__':
    model = net_loader("../assets/")
    digit = cv2.imread('../assets/temp.png', 0)
    digit = digit.reshape((1, 28, 28)).astype('float32')
    digit = digit / 255

    # Predict with model:
    input_data = np.array([digit])
    prediction = model.predict(input_data)
    print(prediction)
