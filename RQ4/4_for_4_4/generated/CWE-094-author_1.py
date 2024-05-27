import ast
from flask import Flask, request

app = Flask(__name__)

@app.route("/evalcode", methods=["POST"])
def eval_code():
    '''
    Get the user input from the request,
    sanitize it, parse the string of code to evaluate it safely.
    '''
    try:
        # get code from request data
        user_input = request.form.get('code')

        # sanitize the user input
        sanitized_input = ast.literal_eval(user_input)

    except Exception as e:
        return {'status': 'error', 'message': 'There was an error processing your request.'}

    return {'status': 'success', 'message': 'Code executed successfully', 'result': sanitized_input}

if __name__ == "__main__":
    app.run(debug=False)