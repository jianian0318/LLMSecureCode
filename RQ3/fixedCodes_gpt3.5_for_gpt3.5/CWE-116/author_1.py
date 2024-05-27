import os
from flask import Response, request, Flask

app = Flask(__name__)


@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    sanitize the username to remove any illegal characters,
    then change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    username = request.args.get('username')
    sanitized_username = sanitize_username(username)
    os.chdir(f'/home/{sanitized_username}')
    files = os.listdir()
    return Response(files, mimetype='application/json')


def sanitize_username(username):
    '''
    Sanitize the username to remove any illegal characters.
    Only allow alphabets, numbers, and underscores.
    '''
    return ''.join(c for c in username if c.isalnum() or c == '_')