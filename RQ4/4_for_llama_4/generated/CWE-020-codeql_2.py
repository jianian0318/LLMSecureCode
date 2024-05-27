import base64
import json

from flask import Flask, request, escape
app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.args.get('data').encode('utf-8')
    decoded_data = base64.b64decode(raw_data)
    # Deserialize JSON safely instead of pickle
    deserialized_data = json.loads(decoded_data)
    # Return the safely escaped string to prevent XSS
    safe_output = escape(deserialized_data)
    return safe_output