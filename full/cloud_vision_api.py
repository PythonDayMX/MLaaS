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

from pprint import pprint
import numpy as np
import requests
import base64
import json
import cv2


def get_raw_img(url):
    """
    Download input image from url.
    """

    pic = False
    response = requests.get(url, stream=True)
    with open('./imgs/img.png', 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
        pic = True
    response.close()
    return pic


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


def consume_vision_api(img_data, flag):
    """
    Consume Google Cloud Vision API via http requests.

    References:
    - https://cloud.google.com/vision/
    - https://cloud.google.com/vision/docs/ocr
    - https://cloud.google.com/vision/docs/request#providing_the_image
    - http://docs.python-requests.org/en/master/user/quickstart/
    """

    # Setup:
    key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    vision_url = 'https://vision.googleapis.com/v1/images:annotate?key=' + key

    # Convert image to base 64:
    if flag not in ('url', 'local'):
        return "ERROR ON INPUT IMAGE!"
    else:
        img = get_as_base64(img_data, flag)
    # print(img)

    # Generate payload:
    value = {
        "requests": [
            {
                "image": {
                    "content": img.decode("utf-8")
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": 5
                    }
                ]
            }
        ]
    }

    # Request to Google Cloud Vision API:
    r = requests.post(vision_url, json=value)

    # Parse and return response:
    response = r.json()
    return response


def parse_response(response):
    """
    Utility function to parse a response into a list.
    """

    elements = []
    for element in response['responses'][0]['labelAnnotations']:
        elements.append(element['description'].capitalize())

    return elements


if __name__ == '__main__':
    # Testing:
    resp = consume_vision_api(img_data='../assets/MLaaS.png', flag='local')
    resp = parse_response(resp)
    print(resp)
