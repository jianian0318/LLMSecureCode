import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    username = request.args.get('username')  # Retrieve the 'username' from the request's arguments
    os.chdir(f'/home/{username}')  # Change the current directory to /home/{username}
    files = os.listdir()  # List all the files
    return Response(str(files), mimetype='text/plain')  # Return the list as a response