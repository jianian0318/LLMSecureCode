import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
    """
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    """
    encoded_name = request.json['first_name']
    decoded_name = base64.b64decode(encoded_name).decode('utf-8')  # decode the base64 string
    setname(decoded_name)  # call setname function

def setname(name):
    """
    A function to set name.
    Add your functionality here.
    """
    pass