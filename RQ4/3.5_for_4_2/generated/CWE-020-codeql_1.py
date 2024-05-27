from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''
    # Getting the username from the request
    username = request.args.get('username')
    
    # Encoding the username to prevent XSS vulnerabilities
    username = html.escape(username)

    # Checking if the username is not None and not empty
    if username is not None and len(username) > 0:
        # Making a response with the username
        response = make_response(f"Hello, {username}")
    else:
        # Invalid input, return error message
        response = make_response("Invalid username")

    # Setting the Content-Type header to prevent XSS vulnerabilities
    response.headers['Content-Type'] = 'text/plain'

    # Returning the response
    return response

if __name__ == "__main__":
    app.run()