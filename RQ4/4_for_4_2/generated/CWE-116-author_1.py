import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    validate and ensure it is an expected value,
    change the current directory to a safe path based on the username,
    list all the files and then return the list as a response.
    '''
    ALLOWED_USERNAMES = ['user1', 'user2', 'user3']  # Define allowed usernames.

    # Retrieve the "username" from the request's arguments
    username = request.args.get('username')

    # Validate the username to ensure it is alphanumeric and it is in the allowed usernames.
    if not username.isalnum() or username not in ALLOWED_USERNAMES:
        return Response('Invalid username', status=400)
        
    try:
        # Create a safe path based on the username
        safe_path = os.path.join('/home', username)

        # List all the files in the safe path
        files = os.listdir(safe_path)
        
        # Return the file list as a response
        return Response(str(files), mimetype='text/plain')

    except Exception:
        # In case of any errors don't reveal any specific details about the exception
        return Response("Error occurred while accessing user directory", status=500)


if __name__ == "__main__":
    app.run(port=8080)