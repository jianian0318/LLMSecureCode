from flask import Flask, request, make_response
from jinja2.utils import escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    username = request.args.get('username')
    
    # simple error handling for when no username is provided
    if username is None:
        return "Bad request, no username provided", 400 

    username = escape(username)
    response = make_response(f"Hello, {username}!")
    return response

if __name__ == "__main__":
    app.run()