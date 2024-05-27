import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute")
def code_execution():
    first_name = request.args.get("first_name")
    decoded_name = base64.b64decode(first_name).decode("utf-8")
    setname(decoded_name)
    return "Name set successfully"

def setname(first_name):
    # code to set the name
    # Fixed code to prevent code injection vulnerability
    sanitized_name = first_name.replace("'", "").replace(";", "")
    # Set the sanitized name
    pass