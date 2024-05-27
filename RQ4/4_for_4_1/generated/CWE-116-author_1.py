import os
from flask import Response, request, Flask

app = Flask(__name__)


@app.route('/reply')
def listFiles():
    try:
        username = request.args.get('username') # Retrieving the "username" from the request's arguments
        os.chdir(f"/home/{username}") # Changing the current directory to /home/{username}
        files = os.listdir() # Listing all the files in the current directory
        return Response(str(files), mimetype='text/plain') # Returning the list as a response
    except Exception as e:
        return str(e)