from flask import Flask, request, make_response
import re
app = Flask(__name__)

@app.route("/profile", methods=['GET'])
def profile():
    username = request.args.get('username')   # Get the username from the request
    if not re.match("^[a-zA-Z0-9_]*$", username): # Validate username
        return 'Invalid Username', 400
    response = make_response(f'Hello {username}')  # Make a response with it
    return response   # Return the response