from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/profile")
def profile():
    username = request.args.get('username')  # Retrieves the 'username' query parameter from the request URL
    response = make_response(username)  # Creates a response with the username
    return response