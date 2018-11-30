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

from flask import Flask, jsonify, request
from mlaas_utils import base64_to_png
from mlaas_utils import net_loader
from pprint import pprint
import numpy as np
import requests
import base64
import json
import cv2

# Main app:
app = Flask(__name__)

# Global:
version = 'v0.0'
model = net_loader("../assets/")


# API MAIN STRUCTURE:
@app.route('/api/' + version, methods=['GET'])
def test():
    """
    GET method to test the API.
    """

    # Output message:
    message = {"response": [{"text": "Hello world!"}]}
    return jsonify(message)


@app.route('/api/' + version + '/predict', methods=['POST'])
def predict():
    """
    POST method to predict with our classification model.
    """

    # Get data from JSON object in POST method:
    req_data = request.get_json()

    # Parse data from JSON:
    img = req_data['base_64']
    img = img.encode()

    # Convert to png and pre-process:
    base64_to_png(img)
    digit = cv2.imread('../assets/temp.png', 0)
    digit = digit.reshape((1, 28, 28)).astype('float32')
    digit = digit / 255

    # Predict with model:
    input_data = np.array([digit])
    prediction = model.predict(input_data)
    prediction = np.argmax(prediction)

    # Output message:
    message = {"response": [
        {"prediction": str(prediction)}
    ]}
    return jsonify(message)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404

    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
