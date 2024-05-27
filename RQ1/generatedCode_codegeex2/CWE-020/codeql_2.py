import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data, store it in a variable and return it
    '''
    raw_data = request.data.decode('utf-8') # Get raw_data from request with utf-8 encoding and decode it with base64.
    decoded_data = base64.b64decode(raw_data) # Decode base64 data
    deserialized_data = pickle.loads(decoded_data) # Deserialize the decoded data, store it in a variable and return it
    return deserialized_data