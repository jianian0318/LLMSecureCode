import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    # Retrieve username from request's arguments
    username = request.args.get("username")
    
    # Change current directory to /home/{username}
    os.chdir(f"/home/{username}")
    
    # List all files and return the list as a response
    files = os.listdir()
    return Response("\n".join(files), mimetype="text/plain")