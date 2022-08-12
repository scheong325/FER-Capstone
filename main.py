#!/usr/bin/env python
import cv2
import json
import numpy as np
from pathlib import Path
from flask import Blueprint, render_template, request
from keras.models import model_from_json

main = Blueprint('main', __name__)

# Load Haarcascade File
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the Path
path = Path.cwd() / "FaceExpressionDetectionFlask" / "ml_folder"

# Load the Model and Weights
model = model_from_json(open(path / "model_structure.json", "r").read())
model.load_weights(path / "model_weights.h5")
model.make_predict_function()


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/welcome', methods=['GET'])
def welcome():
    return render_template('predict.html')


@main.route('/predict', methods=['POST', 'GET'])
def predict():
    from . import classifier
    if request.method == 'POST':
        
        f = request.files['file'].read()
        npimg = np.fromstring(f, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)
        face_properties = classifier.classify(img, face_detector, model)

        return json.dumps(face_properties)


if __name__ == '__main__':

    # Run the flask main app
    main.run()