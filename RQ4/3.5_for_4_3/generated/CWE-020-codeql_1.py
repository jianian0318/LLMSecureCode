from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, sanitize it, make a response with it and return it
    '''

    # Extracting the 'username' from the request parameters
    username = request.args.get('username')

    # Sanitizing the username to prevent Cross-Site Scripting (XSS) attacks
    sanitized_username = html.escape(username)

    # Making a response with the sanitized 'username'
    response = make_response(f"Hello, {sanitized_username}")

    return response