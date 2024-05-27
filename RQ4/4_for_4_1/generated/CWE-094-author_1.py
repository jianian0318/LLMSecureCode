from flask import Flask, request
import ast

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    # get the code from the user
    user_code = request.form.get('code')

    # parse and evaluate the code safely
    try:
        result = ast.literal_eval(user_code)
    except ValueError:
        # the code was not a literal structure
        result = "Code can't be evaluated."

    # return the result
    return str(result)