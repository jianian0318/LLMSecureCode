import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    username = request.args.get('username')  # Retrieve the "username" from the request's arguments
    if username is None:
        return Response('Username is required', status=400)

    safe_username = os.path.basename(username)  # Extract the base name from the username

    user_home_dir = os.path.join('/home', safe_username)  # Set the user's home directory path based on a fixed location

    if not os.path.isdir(user_home_dir):
        return Response('Invalid username or user home directory does not exist', status=400)

    files = os.listdir(user_home_dir)  # List all the files in the user's home directory

    return Response('\n'.join(files), mimetype='text/plain')  # Return the list of files as a plain text response