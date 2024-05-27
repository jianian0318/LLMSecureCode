import base64
import pickle
import json

from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    # Get raw_data from request with utf-8 encoding
    raw_data = request.get_data().decode("utf-8")
    # Ensure input is safe
    safe_data = escape(raw_data)
    # Decode it with base64
    decoded_data = base64.b64decode(safe_data)
    # Deserialize the decoded data
    try:
        # Check if the decoded data is a dictionary
        deserialized_data = json.loads(decoded_data)
        if isinstance(deserialized_data, dict):
            # Convert the deserialized data to JSON string
            json_data = json.dumps(deserialized_data)
            # Return the JSON data
            return json_data, 200, {'Content-Type': 'application/json'}
        else:
            return "Invalid data", 400
    except json.JSONDecodeError as e:
        return "Invalid data", 400

if __name__ == "__main__":
    app.run(debug=True)