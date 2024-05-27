import traceback
from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    user_code = request.form.get('code')  # get user's code from the POST request
    
    # Check if user_code is valid Python code
    if not re.match('^[\w\s\+\-\*\/=\(\)]+$', user_code):
        return "Invalid code"
    
    try:
        # Checking for potential vulnerabilities in the user's code
        if 'os' in user_code or 'subprocess' in user_code or 'exec' in user_code:
            raise Exception('Forbidden code')
        
        # Create a new empty namespace for execution
        namespace = {}
        
        # use eval instead of exec
        result = eval(user_code, namespace)
        
        return "Code executed successfully: {}".format(result)
    except Exception as e:
        return "Error: Forbidden code"  # Remove traceback

if __name__ == "__main__":
    app.run(debug=False)  # Disable Flask debug mode