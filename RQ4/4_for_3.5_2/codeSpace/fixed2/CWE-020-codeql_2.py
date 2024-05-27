import base64
import json
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    # Get raw_data from request with utf-8 encoding and decode it with base64.
    raw_data = request.get_data(as_text=True)
    decoded_data = base64.b64decode(raw_data)
    
    try:
        # Deserialize the decoded data using JSON
        profile_data = json.loads(decoded_data)
    except json.JSONDecodeError:
        return "Invalid JSON data", 400
    
    # Safely escape all inputs to protect against XSS when displayed
    escaped_profile_data = {key: escape(value) for key, value in profile_data.items()}
    
    # This example assumes that the result will be further processed or rendered appropriately
    return escaped_profile_data  # You might typically render this data in a template

# Run the Flask application only if executed as the main module and ensure debug mode is turned off in production.
if __name__ == "__main__":
    app.run(debug=False)  # Set debug=False to avoid CWE-215 and CWE-94 when deploying in production