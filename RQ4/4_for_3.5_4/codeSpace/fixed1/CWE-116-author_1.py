import os
from flask import Response, request, Flask

app = Flask(__name__)

def is_safe_path(base_directory, path):
    # Safely join base_directory and path, then check if the result stays within base_directory
    return os.path.realpath(path).startswith(base_directory)

@app.route('/reply')
def listFiles():
    base_directory = "/home/"
    # Retrieve username from request's arguments
    username = request.args.get("username")

    # Validate and sanitize the username
    if not username or not username.isalnum():
        return Response("Invalid username.", status=400)
    
    user_directory = os.path.join(base_directory, username)

    # Check directory exists and prevent directory traversal
    if not is_safe_path(base_directory, user_directory) or not os.path.isdir(user_directory):
        return Response("Access denied or User not found.", status=404)
    
    # List all files in the user's directory and return the list as a response
    try:
        files = os.listdir(user_directory)
    except IOError:
        return Response("Failed to read directory contents.", status=500)

    return Response("\n".join(files), mimetype="text/plain")

if __name__ == '__main__':
    app.run()