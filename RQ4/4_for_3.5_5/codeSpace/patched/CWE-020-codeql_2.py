import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.get_data(as_text=True)  # Get raw_data from request with utf-8 encoding
    decoded_data = base64.b64decode(raw_data)  # Decode the raw_data with base64
    data = pickle.loads(decoded_data)  # Deserialize the decoded data and store it in a variable
    return data  # Return the deserialized data