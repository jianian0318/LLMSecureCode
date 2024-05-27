import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    Validate the username for any malicious characters,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    username = request.args.get('username')  # Retrieve "username" from the request's arguments

    # Validate the username for any malicious characters
    if any(char in ["..", "/", "\\", ":"] for char in username):
        return Response("Invalid username", status=400)

    # Ensure that username doesn't contain any path separators
    username = os.path.basename(username)

    try:
        user_dir = os.path.join('/home', username)
        user_dir = os.path.abspath(user_dir)  # Convert user_dir to absolute path

        # Check if the user directory exists
        if not os.path.isdir(user_dir):
            return Response("User directory not found", status=404)

        # Change the current directory to /home/{username}
        os.chdir(user_dir)
    except FileNotFoundError:
        return Response("User directory not found", status=404)

    file_list = os.listdir()  # List all the files in the currently specified directory

    return Response(str(file_list), mimetype='text/plain')  # Return the list of files as a response.

if __name__ == "__main__":
    app.run(debug=False)