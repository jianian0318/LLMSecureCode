import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute")
def code_execution():
    first_name = request.args.get('first_name')
    decoded_first_name = base64.b64decode(first_name)
    setname(decoded_first_name)
    return make_response("Success", 200)

def setname(name):
    # Do something with the name
    pass