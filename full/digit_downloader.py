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

from keras.datasets import mnist
from random import randint
import cv2


def digit_downloader(number_of_digits, path):
    """
    Utility funciton to download random digits.
    """

    # Load data:
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Generate random indices:
    digits = [randint(0, 59000) for i in range(number_of_digits)]

    # Save images:
    for digit in digits:
        cv2.imwrite(path + '{}.png'.format(digit), X_train[digit])

    return


if __name__ == "__main__":
    digit_downloader(3, "../assets/")
