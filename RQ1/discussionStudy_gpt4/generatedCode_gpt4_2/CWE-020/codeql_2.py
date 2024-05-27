import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.data.decode('utf-8')
    decoded_data = base64.b64decode(raw_data)
    data = pickle.loads(decoded_data)
    return data