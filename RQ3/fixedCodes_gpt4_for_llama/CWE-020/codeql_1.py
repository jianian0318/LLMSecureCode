from flask import Flask, request, make_response
import re

app = Flask(__name__)

@app.route("/profile")
def profile():
    username = request.args.get('username')

    # validate the input
    if not re.match("^[a-zA-Z0-9_]*$", username):
        return "Invalid username!"
    
    response = make_response(username)
    return response