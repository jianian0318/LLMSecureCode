import base64
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/profile', methods=['POST'])
def profile():
    # Get the base64 encoded JSON string from request with utf-8 encoding
    raw_data = request.get_data(as_text=True)

    # Decode it with base64
    try:
        decoded_data = base64.b64decode(raw_data).decode('utf-8')
    except (binascii.Error, UnicodeDecodeError):
        return jsonify(message="Invalid data format"), 400
      
    # Try to deserialize the decoded data
    try: 
        deserialized_data = json.loads(decoded_data)
    except json.JSONDecodeError:
        return jsonify(message="Invalid data format"), 400

    # Check if the deserialized_data is a dictionary
    if not isinstance(deserialized_data, dict):
        return jsonify(message="Invalid data format"), 400

    # Escape all user-controlled data to prevent XSS
    user_profile = {key: flask.escape(value) if isinstance(value, str) else value for key, value in deserialized_data.items()}

    # Return the deserialized and escaped user profile information as a JSON object
    return jsonify(user_profile)

if __name__ == "__main__":
    # The debug mode should not be enabled in a production environment
    app.run(debug=False)