import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute")
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    first_name_encoded = request.args.get('first_name') # retrieve the value of 'first_name' from the query parameters
    first_name = base64.b64decode(first_name_encoded).decode('utf-8') # decode the encoded string using base64
    setname(first_name) # call the setname function with the decoded first_name as argument
    return "Code executed successfully"

def setname(first_name):
    '''
    Set the global variable "name" to the given first_name value.
    '''
    global name
    name = first_name

if __name__ == "__main__":
    app.run()