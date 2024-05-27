import base64
import json

from flask import Flask, request, escape
app = Flask(__name__)

@app.route("/profile")
def profile():
    # Get the base64-encoded data from the request
    raw_data = request.get_data(as_text=True)
    
    # Safely decode the data from base64, considering it as a simple JSON string
    try:
        decoded_string = base64.b64decode(raw_data).decode('utf-8')
        deserialized_data = json.loads(decoded_string)
    except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
        return "Invalid data provided", 400
    
    # Ensure the deserialized data is a dictionary (JSON object)
    if not isinstance(deserialized_data, dict):
        return "Invalid data format", 400
    
    # Escape all HTML characters to prevent XSS
    safe_data = {key: escape(str(value)) for key, value in deserialized_data.items()}
    
    # Convert dictionary to string representation safely for HTML embedding
    safe_data_representation = "<br>".join(f"{key}: {value}" for key, value in safe_data.items())
    
    return safe_data_representation

if __name__ == "__main__":
    # Run the application without debug mode to prevent arbitrary code execution
    app.run(debug=False)