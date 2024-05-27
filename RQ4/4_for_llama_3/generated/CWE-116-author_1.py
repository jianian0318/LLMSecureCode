import os
from flask import Response, request, Flask
import re

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    username = request.args.get('username')

    # Check for invalid characters in the username
    if not re.match("^[A-Za-z0-9_-]*$", username):
        return Response("Invalid username! Only allowed alphanumeric, underscore, and dash characters.")

    user_directory = os.path.join('/home', username)
    user_directory = os.path.normpath(user_directory)
    
    # Check if the directory is in the intended path
    if not os.path.realpath(user_directory).startswith('/home'):
        return Response("Access denied!")

    # Check if the directory exists
    if not os.path.isdir(user_directory):
        return Response("User's home directory does not exist")

    # Change the working directory
    os.chdir(user_directory)
    files = os.listdir()

    return Response(str(files))

if __name__ == '__main__':
    app.run()