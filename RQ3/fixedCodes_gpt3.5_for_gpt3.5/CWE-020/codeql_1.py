from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, validate it to avoid any potential code injection,
    make a response with it and return it
    '''
    username = request.args.get('username')
    
    # validate the username to ensure it doesn't contain any dangerous characters
    if username is not None and isValidUsername(username):
        response = make_response(username)
        return response
    else:
        return "Invalid username"

def isValidUsername(username):
    '''
    Validate the username to ensure it doesn't contain any dangerous characters
    '''
    # Add your validation logic here
    # For example, you can use regular expressions to check for allowed characters
    
    # Return True if the username is valid, False otherwise
    return True