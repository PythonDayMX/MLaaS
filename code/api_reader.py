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
    Download JSON response url.
    """

    # Get response:
    # TODO

    # If response's status is 200:
    if response.status_code == requests.codes.ok:
        # Pretty print response:
        # TODO

        # Save response into a JSON file:
        # TODO
        pass
    return


def get_prediction(url, filename):
    """
    Download JSON response url for prediction.
    """

    # Set metadata:
    headers = {'Content-type': 'application/json'}
    input_values = {'sepal_length': 5.1,
                    'sepal_width': 3.5,
                    'petal_length': 1.4,
                    'petal_width': 0.2}

    # Get response:
    # TODO

    # If response's status is 200:
    if response.status_code == requests.codes.ok:
        # Pretty print response:
        # TODO

        # Save response into a JSON file:
        # TODO
        pass
    return


if __name__ == '__main__':
    # Try out our JSON response downloader:
    get_json('http://localhost:5000/api/v0.0', 'response.json')
    get_prediction('http://localhost:5000/api/v0.0/predict', 'response.json')
