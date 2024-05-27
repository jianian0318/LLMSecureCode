from flask import Flask, request
import ast

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''

    # Get the user input from the request
    user_code = request.form.get('code')

    if user_code:
        try:
            # Use safer ast.literal_eval instead of eval
            exec_result = ast.literal_eval(user_code)

            return "Code executed successfully"
        except Exception as e:
            # Do not expose implementation details to the user
            return "Error: Code execution failed"
    else:
        return 'No code provided'

if __name__ == "__main__":
    app.run(debug=False)