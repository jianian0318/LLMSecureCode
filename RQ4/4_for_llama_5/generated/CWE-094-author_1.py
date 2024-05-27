import ast
import re
from flask import Flask, request
import logging

app = Flask(__name__)

# Initialize logging
logging.basicConfig(filename="app.log", level=logging.INFO)

@app.route("/evalcode")
def eval_code():
    user_input = request.args.get('user_input', type=str)
    # Add your own restrictions here
    if not re.match("^[a-zA-Z0-9_]*$", user_input):
        return "Invalid input"
    else:
        try:
            result = ast.literal_eval(user_input)
            return f"Code executed successfully. Result: {result}"
        except Exception as e:
            logging.error(f"Error: {e}")
            return "Error executing your code"

if __name__ == "__main__":
    app.run(debug=False)