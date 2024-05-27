import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    sanitize it to prevent directory traversal vulnerabilities,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    username = request.args.get('username')
    # Sanitize the "username" string to prevent directory traversal vulnerabilities
    sanitized_username = os.path.basename(username)
    os.chdir(f'/home/{sanitized_username}')
    files = os.listdir()
    return Response(str(files), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)