import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    username = request.args.get('username')
    if username is None:
        return Response("Username not provided", status=400)

    try:
        username = username.replace("..", "")   # Remove any '..', which could be used for directory traversal attack
        username = os.path.abspath(username)    # Get the absolute path of the username to prevent file access outside the specified directory
        os.chdir(f'/home/{username}')           # Change the current directory to /home/{username}
        files = os.listdir()
        files = "\n".join(files)                 # Convert the list of files into a string with newline separator
        return Response(files)
    except FileNotFoundError:
        return Response(f"User {username} not found", status=404)
    except Exception as e:
        return Response(str(e), status=500)