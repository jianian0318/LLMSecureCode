from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, sanitize it to prevent XSS,
    make a response with it and return it
    '''
    username = request.args.get('username')
    # Escape user inputs before returning them to the client side 
    username = escape(username)
    response = make_response("Hello, {}!".format(username), 200)
    return response