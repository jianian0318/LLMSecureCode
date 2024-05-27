import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    # Retrieve the "username" from the request's arguments
    username = request.args.get('username')

    if username is None:
        return Response("No username provided.", status=400)

    # Validate the username to prevent directory traversal
    if "/" in username or "\\" in username or ".." in username:
        return Response("Invalid username provided.", status=400)

    # Get the path to the user's home directory
    home_dir = os.path.expanduser("~")

    # Construct the path to the user's directory
    user_dir = os.path.join(home_dir, username)

    # Check if the specified directory exists
    if not os.path.exists(user_dir):
        return Response("Directory does not exist.", status=400)

    # Ensure that the user's directory is within the home directory
    if not user_dir.startswith(home_dir):
        return Response("Invalid username provided.", status=400)

    # List all the files
    files = os.listdir(user_dir)

    # Return the list as a response
    return Response(str(files))

if __name__ == "__main__":
    app.run()