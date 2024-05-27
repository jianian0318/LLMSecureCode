from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    username = request.args.get('username')  # Retrieves the 'username' query parameter from the request URL
    if username:
        safe_username = escape(username)  # Escaping special HTML characters
    else:
        safe_username = "Anonymous"
    response = make_response(f"Welcome, {safe_username}!")  # Creates a response with the sanitized username
    return response

if __name__ == "__main__":
    app.run(debug=True)