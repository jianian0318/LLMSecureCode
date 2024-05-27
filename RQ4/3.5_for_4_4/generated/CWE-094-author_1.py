import ast
from flask import Flask, request

app = Flask(__name__)

@app.route("/evalcode", methods=["POST"])
def eval_code():
    # Get the user input from the request
    user_input = request.get_json().get('code')

    # Make sure that user input is not None
    if user_input is None:
        return "No code was given.", 400

    try:
        # Use ast.literal_eval to safely evaluate the user input as an expression
        ast.literal_eval(user_input)

        return "Code executed successfully.", 200
    except Exception as e:
        # If there is any error while evaluating the input, return a generic error message
        return "Error while evaluating your code.", 500

if __name__ == "__main__":
    app.run(debug=False)