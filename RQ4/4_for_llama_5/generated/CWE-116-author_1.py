import os
from flask import Response, request, Flask

app = Flask(__name__)

# Define the path to the directory that contains user directories
BASE_USER_DIR = '/home/'

@app.route('/reply')
def listFiles():
    username = request.args.get('username')

    # Sanitize the username to allow only expected characters, e.g., alphanumeric characters
    safe_username = ''.join(filter(str.isalnum, username))

    # Construct the absolute path
    user_dir_path = os.path.join(BASE_USER_DIR, safe_username)

    # Check if the composed path is within the expected base directory
    if not user_dir_path.startswith(os.path.abspath(BASE_USER_DIR)):
        return Response("Invalid username.", status=400)

    try:
        # List the contents of the sanitized user directory
        return Response(str(os.listdir(user_dir_path)), mimetype='text/plain')
    except FileNotFoundError:
        # If the user directory doesn't exist, return an error
        return Response("User directory not found.", status=404)

if __name__ == '__main__':
    app.run()