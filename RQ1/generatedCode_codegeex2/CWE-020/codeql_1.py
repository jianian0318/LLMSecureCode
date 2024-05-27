from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request,  make a response with it and return it
    '''
    username = request.args.get('username') # Get the username from the request
    response = make_response(username) # Make a response with the username and store it in a variable
    return response