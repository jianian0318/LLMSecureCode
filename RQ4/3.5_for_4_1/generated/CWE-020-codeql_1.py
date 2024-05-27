from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, escape it, make a response with it and return it
    '''
    username = request.args.get('username')  # Get username from request arguments
    escaped_username = escape(username)  # Escape username to prevent XSS vulnerability
    response = make_response(f'Hello {escaped_username}')  # create a response containing username
    return response  # return the response