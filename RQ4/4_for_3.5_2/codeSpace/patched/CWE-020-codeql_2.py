import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    # Get raw_data from request with utf-8 encoding and decode it with base64.
    raw_data = request.data.decode('utf-8')
    decoded_data = base64.b64decode(raw_data).decode('utf-8')  # Decode base64
    # Deserialize the decoded data, store it in a variable and return it
    profile_data = pickle.loads(decoded_data)
    
    return profile_data