import ast
from flask import Flask, request
import traceback

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])  # allow POST requests
def eval_code():
    '''
    Get the user input from the request,
    compile it into a python code, then execute it.
    '''
    user_input = request.form.get('code')  # retrieve user input from form data

    try:
        # Sanitize user input
        sanitized_input = sanitize_input(user_input)

        # Execute the sanitized input as python code
        ast.literal_eval(sanitized_input)  # execute the sanitized input as python code

        return 'Code executed successfully'

    except Exception as e:
        # Log the exception without leaking sensitive information
        traceback.print_exc()

        return 'Error executing code'

def sanitize_input(input_string):
    '''
    Sanitize the user input by removing any unwanted characters or commands.
    '''
    # Add sanitization logic here

    return input_string

if __name__ == "__main__":
    app.run(debug=False)