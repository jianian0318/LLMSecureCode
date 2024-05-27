import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    sanitize the username to prevent any directory traversal,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.

    Any occurring error will be caught and returned as response.
    '''
    try:
        # Retrieve the "username" from the request's arguments
        username = request.args.get('username')

        # Sanitize the username to prevent any directory traversal
        sanitized_username = sanitize(username)

        # Change the current directory to /home/{username} if the username is not None or empty
        if sanitized_username:
            home_directory = os.path.join('/home', sanitized_username)
            # validate path
            if os.path.isdir(home_directory):
                os.chdir(home_directory)
            else:
                return 'Invalid username'

        # List all the files
        files_list = os.listdir()

        # Return the file list as a response
        return Response(', '.join(files_list), mimetype='text/plain')

    except Exception as e:
        # Return a generic error message as response
        return 'An error occurred while listing files.'

def sanitize(username):
    '''
    Sanitize the input username to prevent any directory traversal.
    Only allow alphanumeric characters, underscores, and hyphens.
    '''
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    sanitized_username = ''.join(c for c in username if c in allowed_characters)
    return sanitized_username

if __name__ == '__main__':
    app.run()