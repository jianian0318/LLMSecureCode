from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/profile", methods=['GET'])
def profile():
    username = request.args.get('username')   # Get the username from the request
    response = make_response(f'Hello {username}')  # Make a response with it
    return response   # Return the response