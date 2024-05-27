import base64
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    first_name = request.form.get("first_name")
    decoded_first_name = base64.b64decode(first_name).decode('utf-8')
    setname(decoded_first_name)
    response = make_response()
    response.status_code = 200
    return response

def setname(first_name):
    '''
    This function can be implemented later.
    '''
    pass

if __name__ == "__main__":
    app.run()