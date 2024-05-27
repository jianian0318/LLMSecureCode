from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    # Extract the username from the request and escape it
    username = escape(request.args.get('username'))

    # Create a response with the username
    response = make_response("Welcome, {}!".format(username))

    # Return the response
    return response