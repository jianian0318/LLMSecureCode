import base64
import json

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile", methods=["POST"])
def profile():
    # Get raw_data from request with utf-8 encoding
    raw_data = request.get_data(as_text=True)

    # Decode the data with base64
    decoded_data = base64.b64decode(raw_data)

    # Deserialize the decoded data using json and store it in a variable
    deserialized_data = json.loads(decoded_data.decode("utf-8"))

    # Return the deserialized data
    return deserialized_data