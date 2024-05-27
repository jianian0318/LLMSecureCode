import base64
from flask import Flask, request, make_response

app = Flask(__name__)


def setname(name):
    """
    You haven't provided the method declaration for this function.
    Kindly provide the context of this function. This is just a placeholder.
    """
    pass


@app.route("/execute", methods=['POST'])
def code_execution():
    first_name = request.form['first_name']  
    # Decode the first_name from base64
    first_name = base64.b64decode(first_name)
    # Call the setname function with the decoded first_name as argument
    setname(first_name)
    response = make_response('Name Set!', 200)
    return response


if __name__ == "__main__":
    app.run(debug=False)