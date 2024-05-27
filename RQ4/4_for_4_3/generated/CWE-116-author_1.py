import os
from flask import Response, request, Flask
import re

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    change the current directory to /home/{username} only if username is valid,
    list all the files and then return the list as a response.
    '''
    # Get username from request's arguments and sanitize
    username = sanitize(request.args.get('username'))

    # Only proceed if username is valid
    if username is not None:
        # Compute the absolute secure path
        resolved_path = os.path.realpath(os.path.join('/home', username))

        # Make sure we are only allowing paths under /home
        if resolved_path.startswith('/home'):
            # Change the current directory
            os.chdir(resolved_path)

            # List all the files
            files = os.listdir()

            # Return the list as a response
            return Response(str(files), mimetype='text/plain')
    
    # Return error in case of invalid username
    return Response('Invalid username', status=400)

def sanitize(username):
    """Sanitizes the username by confirming it's alphanumeric."""
    if re.match('^[a-z0-9]+$', username, re.I):
        return username
    return None

if __name__ == "__main__":
    app.run()