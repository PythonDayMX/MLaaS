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
import pprint
import json


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


def get_prediction(url, filename):
    """
    Download JSON response url for prediction.
    """

    # Set metadata:
    headers = {'Content-type': 'application/json'}
    input_values = {'sepal_length': 6.4,
                    'sepal_width': 3.2,
                    'petal_length': 4.5,
                    'petal_width': 1.5}

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
    get_json('http://localhost:5000/api/v0.0', 'response.json')
    get_prediction('http://localhost:5000/api/v0.0/predict', 'response.json')
