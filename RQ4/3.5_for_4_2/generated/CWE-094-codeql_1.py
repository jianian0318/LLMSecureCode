import base64
from flask import Flask, request
import html

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def code_execution():
    # Get "first_name" from the post request object
    first_name = request.get_json().get('first_name')
    
    # Encode the string using base64
    first_name_encoded = base64.b64encode(first_name.encode('utf-8')).decode('utf-8')

    # Call the setname function with the encoded first_name as argument
    return setname(first_name_encoded)


def setname(name):
    # This is a dummy function, replace it with your actual function
    
    # Sanitize the user input to prevent cross-site scripting vulnerability
    sanitized_name = html.escape(name)
    
    return f'Hello, {sanitized_name}!'