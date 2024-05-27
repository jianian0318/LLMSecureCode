from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/profile", methods=['GET'])
def profile():
    username = request.args.get('username')   # Get the username from the request
    if username is None:
        return "Username is missing", 400   # Return an error response if username is missing
    response = make_response(f'Hello {username}')  # Make a response with the provided username
    return response   # Return the response with the username provided by the user