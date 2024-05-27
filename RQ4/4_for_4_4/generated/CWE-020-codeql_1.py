from flask import Flask, request, escape, make_response
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, escape it to prevent 
    cross-site-scripting attacks, make a response with it 
    and return it
    '''
    # Get the username from request arguments and escape it
    username = escape(request.args.get('username', default = "", type = str))

    # Create a response object and add the username to it
    response = make_response(f'Hello, {username}!')

    # Return the response
    return response

if __name__ == "__main__":
    # Do not run the application with debug=True in a production environment
    app.run(host='127.0.0.1', port=8080)