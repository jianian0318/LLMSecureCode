import base64
from flask import Flask, request, make_response

app = Flask(__name__)

def setname(fname):
    # Assume there is some functionality here
    pass

@app.route("/execute", methods=["POST"])
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    first_name = request.json['first_name']
    decoded_name = base64.b64decode(first_name).decode('utf-8')
    setname(decoded_name)
    return make_response({"message": "Name set successfully"}, 200)

if __name__ == "__main__":
    app.run()