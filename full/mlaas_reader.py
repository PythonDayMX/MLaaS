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

import requests
import base64
import pprint
import json
import cv2


def get_as_base64(url, flag):
    """
    Convert input image into base64.
    """

    if flag == 'url':
        return base64.b64encode(requests.get(url).content)
    if flag == 'local':
        image = cv2.imread(url)
        _, image = cv2.imencode('.png', image)
        return base64.b64encode(image)


def get_json(url, filename):
    """
    Download JSON response url for testing.
    """

    # Get response:
    response = requests.get(url)

    # If response's status is 200:
    if response.status_code == requests.codes.ok:
        # Pretty print response:
        pprint.pprint(response.json())

        # Save response into a JSON file:
        with open(filename, 'wt') as output:
            output.write(response.text)
    return


def get_prediction(img, url, filename):
    """
    Download JSON response url for prediction.
    """

    # Convert image to base64:
    digit = get_as_base64(img, 'local')
    digit = digit.decode("utf-8")

    # Set metadata:
    headers = {'Content-type': 'application/json'}
    input_values = {'base_64': digit}

    # Get response:
    response = requests.post(url, json=input_values, headers=headers)

    # If response's status is 200:
    if response.status_code == requests.codes.ok:
        # Pretty print response:
        pprint.pprint(response.json())

        # Save response into a JSON file:
        with open(filename, 'wt') as output:
            output.write(response.text)
    return


if __name__ == '__main__':
    # Try out our JSON response downloader:
    get_json('http://localhost:5000/api/v0.0',
             'response.json')

    get_prediction('../assets/21628.png',
                   'http://localhost:5000/api/v0.0/predict',
                   'response.json')
