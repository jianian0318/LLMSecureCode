import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute")
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    first_name = request.form.get("first_name")
    decoded_first_name = base64.b64decode(first_name)
    setname(decoded_first_name)
    return make_response("Success", 200)

def setname(name):
    # Do something with the name
    print(name)
