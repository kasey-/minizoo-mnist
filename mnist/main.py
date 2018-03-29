from flask import Flask
from flask_cors import CORS
from flask import request

import keras.models
from keras.models import load_model

from scipy.misc import imread, imresize
import numpy as np
import re
import base64
from io import BytesIO

global model
model = load_model('model/model.h5')

app = Flask(__name__)
CORS(app)

def convertImage(data):
    img = re.search(r'base64,(.*)', str(data)).group(1)
    img = base64.b64decode(img)
    return img

def reshapeData(data):
    x = np.invert(data)
    x = imresize(x, (28, 28))
    x = x.astype('float32')
    x /= 255
    return x.reshape(1, 1, 28, 28)

@app.route('/mnist/number', methods=["POST"])
def predict():
    img = convertImage(request.form['img'])
    x = imread(BytesIO(img), mode='L')
    x = reshapeData(x)
    prediction = model.predict(x)
    return np.array_str(np.argmax(prediction, axis=1))
