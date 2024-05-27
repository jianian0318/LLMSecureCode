import base64
import json

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    '''
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data, store it in a variable and sanitize it.
    Return the sanitized data.
    '''
    # Get data from request and validate it
    raw_data = request.data.decode('utf-8')
    
    # Perform input validation
    if not is_valid_input(raw_data):
        return "Invalid input"
    
    # Decode the data with base64
    decoded_data = base64.b64decode(raw_data)
    
    # Deserialize the decoded data
    try:
        deserialized_data = json.loads(decoded_data)
    except json.JSONDecodeError:
        return "Error occurred while deserializing data"
    
    sanitized_data = sanitize_input(deserialized_data)
    return sanitized_data

def is_valid_input(data):
    '''
    Validate the input data to prevent cross-site scripting vulnerability.
    '''
    # Implement your validation logic here
    if "<script>" in data:
        return False
    
    return True

def sanitize_input(data):
    '''
    Sanitize the input data to prevent cross-site scripting vulnerability.
    '''
    # Implement your sanitization logic here
    sanitized_data = {}
    for key, value in data.items():
        sanitized_data[key] = escape(value)
    
    return sanitized_data

if __name__ == "__main__":
    app.run(debug=False)