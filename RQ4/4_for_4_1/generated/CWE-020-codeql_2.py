import base64
import json

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    try:
        # Get raw_data from request
        raw_data = request.data.decode('utf-8')

        # Decode raw_data with base64
        decoded_data = base64.b64decode(raw_data)

        # Deserialize the data
        deserialized_data = json.loads(decoded_data)

        # Return the deserialized data
        return str(deserialized_data)
    except Exception as e:
        return 'An error occurred: ' + str(e)