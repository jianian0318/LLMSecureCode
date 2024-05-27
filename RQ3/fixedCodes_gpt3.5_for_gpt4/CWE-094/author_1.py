# Importing necessary modules from flask
from flask import Flask, request
# Initializing Flask app
app = Flask(__name__)

# Defining app route for evaluating user input as code
@app.route("/evalcode", methods=['POST'])
def eval_code():
    # Get the user input from the request as python code
    user_code = request.form.get('code')
    
    # Add a fix to prevent Code Injection
    if "__" in user_code:
        return "Invalid input"
    
    # Now, compile the user code
    compiled_code = compile(user_code, "<string>", "exec")
    # Execute the compiled code
    exec(compiled_code)
    
    return "Code executed successfully"

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server. 
    app.run()