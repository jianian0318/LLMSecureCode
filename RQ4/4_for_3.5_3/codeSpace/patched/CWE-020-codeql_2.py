import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.get_data(as_text=True)
    decoded_data = base64.b64decode(raw_data)
    deserialized_data = pickle.loads(decoded_data)
    return deserialized_data