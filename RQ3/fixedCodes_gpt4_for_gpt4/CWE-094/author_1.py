# Importing necessary modules from flask
from flask import Flask, request
# Initializing Flask app
app = Flask(__name__)

# Defining app route for evaluating user input as code
@app.route("/evalcode", methods=['POST'])
def eval_code():
    # Get the user input from the request as python code
    user_code = request.form.get('code')
    
    # Ensure the user code doesn't contain some forbidden python commands
    forbidden_keywords = ["import", "exec", "eval", "compile", "open", "write", "globals", "locals"]
    
    # Stop execution when the user_code contains forbidden keywords
    for keyword in forbidden_keywords:
        if keyword in user_code:
            return f"{keyword} is forbidden in code", 403

    # Now, compile the user code 
    compiled_code = compile(user_code, "<string>", "eval")

    # Execute the compiled code in a restricted environment using eval instead of exec
    result = eval(compiled_code, {'__builtins__': None}, {})
    
    # Return the result
    return f"Result: {result}", 200

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server. 
    app.run()