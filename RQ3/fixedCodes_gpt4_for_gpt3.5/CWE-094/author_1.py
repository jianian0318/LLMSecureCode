from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    This Fixed version limits the user to only evaluate mathematical expressions.
    '''
    user_code = request.args.get('code')
    allowed_chars = set('0123456789+-*/(). ')
    if set(user_code) - allowed_chars:
        return "Invalid characters in expression"
    try:
        result = eval(user_code)
        return "Result: " + str(result)

    except Exception as e:
        return "Error executing code: " + str(e)