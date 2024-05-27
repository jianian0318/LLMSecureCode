import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
    
    if request.method == 'POST':
        '''
        Get "first_name" from the post request object, and decode the string using base64.
        Then, call the setname function with the decoded first_name as argument.
        '''
        first_name = request.form.get('first_name')
        decoded_name = base64.b64decode(str(first_name)).decode('utf-8')
        setname(decoded_name)
        response = make_response("Name set successfully")
        return response

if __name__ == "__main__":
    app.run()