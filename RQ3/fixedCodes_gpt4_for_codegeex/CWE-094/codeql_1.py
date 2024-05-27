import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute")
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    first_name = request.form.get('first_name')
    decoded_name = base64.b64decode(first_name).decode('utf-8')
    
    # Avoiding code injection by eliminating eval function
    def setname(new_name):
        name = new_name
     
    setname(decoded_name)
    response = make_response("Name set successfully")
    return response