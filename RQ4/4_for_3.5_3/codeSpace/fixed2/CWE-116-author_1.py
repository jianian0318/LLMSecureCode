import os
from flask import Response, request, Flask

app = Flask(__name__)

# Set a safe base directory
BASE_DIR = "/home"

@app.route('/reply')
def list_files():
    # Retrieve the "username" from the request's arguments
    username = request.args.get('username')
    
    # Validate username and construct a safe path
    if username is None:
        return Response("Username is missing!", status=400)

    # Construct the path
    user_path = os.path.join(BASE_DIR, username)

    # Prevent directory traversal
    if not os.path.normpath(user_path).startswith(os.path.abspath(BASE_DIR)):
        return Response("Access denied!", status=403)
    
    # Check if the path exists and is a directory
    if not os.path.isdir(user_path):
        return Response("No such directory!", status=404)

    # List all the files in the directory safely
    try:
        files = os.listdir(user_path)
    except Exception:
        # Do not leak information about the exception
        return Response("Error reading directory", status=500)
    
    # Return the list as a response
    return Response('\n'.join(files), mimetype='text/plain')

if __name__ == "__main__":
    # Run the application without debug mode for production
    app.run(debug=False)