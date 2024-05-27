import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    first_name_encoded = request.json["first_name"]
    first_name = base64.b64decode(first_name_encoded).decode()
    setname(first_name)
    return make_response({"message": "success"}, 200)


def setname(name):
    '''
    This is a placeholder function that should be replaced with actual functionality.
    '''
    print("The first name is: ", name)
      

if __name__ == "__main__":
    app.run()