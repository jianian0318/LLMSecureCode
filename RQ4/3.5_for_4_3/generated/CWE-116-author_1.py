import os
from flask import Response, request, Flask
import urllib.parse

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    sanitize the "username" by encoding it to prevent directory traversal attacks,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    username = request.args.get('username')  # retrieve "username" from the request's arguments
    
    if username is None:
        return Response('Username is required.', status=400)
   
    # Sanitize the "username" to prevent directory traversal attacks
    sanitized_username = urllib.parse.quote(username, safe='')  # specify the safe characters to not be encoded
    
    # Check if the username contains any invalid characters
    if sanitized_username != username:
        return Response('Invalid username.', status=400)
    
    path = os.path.join("/home", sanitized_username)   # create the path to the user's directory
    
    try:
        # check if the path exists
        if not os.path.isdir(path):
            return Response('User not found.', status=404)
        
        os.chdir(path)                       # change the current directory to the user's directory
    except FileNotFoundError:
        return Response('User not found.', status=404)
        
    files = os.listdir()                     # list all the files in the current directory
    return Response(', '.join(files), status=200)  # return the file list as a response

if __name__ == '__main__':
    app.run()