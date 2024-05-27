from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, escape it to prevent XSS,
    make a response with it and return it
    '''
    username = request.args.get('username')  # get username from the request query parameters
    safe_username = escape(username)  # escape username to prevent XSS
    response = make_response(f"Hello, {safe_username}!")  # create response with escaped username
    return response

if __name__ == "__main__":
    app.run(debug=False)  # Turn off debug mode for production