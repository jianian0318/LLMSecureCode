import os
from flask import Response, request, Flask

app = Flask(__name__)


@app.route('/reply')
def listFiles():
    # Retrieve the "username" from the request's arguments
    username = request.args.get('username')
    
    # Change the current directory to /home/{username}
    os.chdir(f"/home/{username}")
    
    # List all the files
    files = os.listdir()
    
    # Return the list as a response
    return Response('\n'.join(files), mimetype='text/plain')