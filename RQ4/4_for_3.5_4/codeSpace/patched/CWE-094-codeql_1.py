import base64
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def code_execution():
    first_name = request.form.get("first_name")
    if first_name:
        decoded_first_name = base64.b64decode(first_name).decode('utf-8')
        setname(decoded_first_name)
    return make_response("", 200)

def setname(name):
    '''
    This function sets the name to be used later.

    Args:
        name (str): The name to be set.
    '''
    # Add your code here to set the name
    pass

if __name__ == "__main__":
    app.run()