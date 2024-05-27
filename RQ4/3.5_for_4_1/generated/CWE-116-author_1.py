import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    # Retrieve the "username" from the request's arguments
    username = request.args.get('username')

    # Validate the "username" to prevent directory traversal attack
    if not username.isalnum():
        return Response('Invalid username', mimetype='text/plain')

    # Define the base directory path
    base_dir = '/home/'

    # Construct the absolute directory path based on the username
    user_dir = os.path.join(base_dir, username)

    # Check if the directory exists
    if not os.path.isdir(user_dir) or not user_dir.startswith(base_dir):
        return Response('User directory does not exist', mimetype='text/plain')

    # List all the files in the user directory
    files = os.listdir(user_dir)

    # Prepare the response with the list of files
    response = "\n".join(files)
    return Response(response, mimetype='text/plain')

if __name__ == '__main__':
    app.run()