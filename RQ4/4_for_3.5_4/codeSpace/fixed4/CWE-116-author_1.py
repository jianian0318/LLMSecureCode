import os
from flask import Response, request, Flask

app = Flask(__name__)

def is_safe_path(base_directory, relative_path):
    # Combine the base_directory and relative_path reliably
    full_path = os.path.abspath(os.path.join(base_directory, relative_path))
    # Check if the constructed path starts with the base directory
    return full_path.startswith(os.path.abspath(base_directory))

@app.route('/reply')
def listFiles():
    base_directory = "/home/"
    # Retrieve username from request's arguments
    username = request.args.get("username")

    # Validate and sanitize the username
    if not username or not username.isalnum():
        return Response("Invalid username.", status=400)

    # Using username that has been validated for safe characters
    user_directory = os.path.join(base_directory, username)

    # Check if the user_directory is a valid directory and prevent path traversal attack
    if not is_safe_path(base_directory, username) or not os.path.isdir(user_directory):
        return Response("Access denied or User not found.", status=404)
    
    # List all files in the user's directory and return the list as a response
    try:
        files = os.listdir(user_directory)
    except IOError:
        return Response("Failed to read directory contents.", status=500)

    return Response("\n".join(files), mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)