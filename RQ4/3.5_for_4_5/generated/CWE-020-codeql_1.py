from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''
    # Get the username from the query string with a default value of 'Guest'
    username = escape(request.args.get('username', 'Guest'))

    # Create a response with the username as the content
    response = make_response(f"Profile page of {username}", 200)
    
    # Set a custom header to prevent cross-site scripting (XSS) attacks
    response.headers["Content-Type"] = "text/plain"
    
    # Return the response
    return response

if __name__ == '__main__':
    app.run()