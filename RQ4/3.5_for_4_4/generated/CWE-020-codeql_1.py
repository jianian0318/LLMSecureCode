from flask import Flask, request, make_response
import html

app = Flask(__name__)


@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''
    # Get the 'username' from the request's arguments
    username = request.args.get('username')

    # Make a response with the sanitized username and return it
    sanitized_username = html.escape(username)
    response = make_response(f'Username: {sanitized_username}', 200)
    
    return response