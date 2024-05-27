from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/profile", methods=['GET'])
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''
    # Get 'username' from request arguments
    username = request.args.get('username')

    # Make a response with the username
    response = make_response(f'Username received: {username}')

    return response

if __name__ == '__main__':
    app.run(debug=False)