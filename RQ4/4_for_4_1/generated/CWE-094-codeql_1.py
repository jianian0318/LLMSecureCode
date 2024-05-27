import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute", methods = ["POST"])
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''

    # Get "first_name" from the post request object
    first_name_encoded = request.form['first_name']

    # Decode the string using base64
    first_name = base64.b64decode(first_name_encoded).decode('utf-8')

    # Calling the setname function (it should be predefined)
    setname(first_name)

    return make_response("Success", 200)

if __name__ == "__main__":
    # Set debug mode to False while running in production
    app.run(debug=False)