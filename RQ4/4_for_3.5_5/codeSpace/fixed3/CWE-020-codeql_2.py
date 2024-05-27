import base64
import json
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/profile", methods=["POST"])
def profile():
    # Get raw_data from request with utf-8 encoding
    raw_data = request.get_data(as_text=True)
    # Decode the raw_data with base64
    decoded_data = base64.b64decode(raw_data)
    # Deserialize the decoded data with a secure format such as JSON and store it in a variable
    try:
        data = json.loads(decoded_data)
    except json.JSONDecodeError:
        return "Invalid JSON data", 400
    
    # Safely escape user input before returning it to prevent XSS attacks
    escaped_data = {k: escape(v) if isinstance(v, str) else v for k, v in data.items()}
    
    return str(escaped_data)  # Return the sanitized deserialized data

if __name__ == "__main__":
    app.run(debug=False)  # Disable debug mode for secure deployment