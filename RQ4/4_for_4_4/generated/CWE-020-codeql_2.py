import base64
import json

from flask import Flask, request, escape
app = Flask(__name__)

@app.route("/profile")
def profile():
    # Get raw_data from request with utf-8 encoding
    raw_data = request.data.decode("utf-8")
    # decode it with base64
    decoded_data = base64.b64decode(raw_data)
    # Load the decoded data safely using json.loads()
    data = json.loads(decoded_data)
    # Escape the data to prevent XSS attacks
    safe_data = escape(data)
    # store it in a variable and return it
    return safe_data