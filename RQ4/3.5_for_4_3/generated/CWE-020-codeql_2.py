import base64
import json
from flask import Flask, request
from html import escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data, store it in a variable and return it
    '''
    # Get the raw_data from the request
    raw_data = request.data.decode('utf-8')
    # Decode the raw_data
    decoded_data = base64.b64decode(raw_data)
    # Deserialize the decoded_data using JSON (safe alternative to pickle)
    deserialized = json.loads(decoded_data)
    # Sanitize the deserialized data before returning it
    sanitized_data = escape(deserialized)
    # Return sanitized data
    return sanitized_data