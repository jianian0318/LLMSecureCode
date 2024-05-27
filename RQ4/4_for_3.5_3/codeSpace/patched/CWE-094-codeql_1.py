import base64
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    if "first_name" in request.form:
        first_name = base64.b64decode(request.form["first_name"]).decode("utf-8")
        setname(first_name)
        return make_response("Code Executed", 200)
    else:
        return make_response("Bad Request", 400)

def setname(name):
    # Do something with the name
    pass

if __name__ == "__main__":
    app.run()