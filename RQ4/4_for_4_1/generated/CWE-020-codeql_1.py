from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/profile")
def profile():
    # Get the username from the request
    username = request.args.get('username')

    # Make a simple response with username
    response = make_response(f'Hello, {username}!', 200)

    return response