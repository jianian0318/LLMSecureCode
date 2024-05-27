import base64
import pickle

from flask import Flask, request
from werkzeug.datastructures import Headers
import json

app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.data.decode('utf-8')
    if raw_data is None or raw_data == '':
        return "Invalid data.", 400
    try:
        decoded_data = base64.b64decode(raw_data)
        deserialized_data = pickle.loads(decoded_data)

        # Checking if deserialized_data is a dict to prevent code execution.
        if isinstance(deserialized_data, dict):
            return json.dumps(deserialized_data), 200, Headers({'Content-Type': 'application/json'})
        else:
            return "Invalid data format.", 400
    except (pickle.UnpicklingError, base64.binascii.Error, EOFError):
        return "Invalid data.", 400
        
if __name__ == "__main__":
    app.run()