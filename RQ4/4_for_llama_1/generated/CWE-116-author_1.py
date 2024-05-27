import os
from flask import Response, request, Flask

app = Flask(__name__)

# Prevent directory traversal (CWE-643) by restricting the characters allowed in usernames.
def sanitize_username(username):
    return ''.join(c for c in username if c.isalnum())

@app.route('/reply')
def list_files():
    username = request.args.get('username')
    if username:
        username = sanitize_username(username)
        user_directory = os.path.join('/home', username)
        # Only allow listing files if the directory exists
        if os.path.isdir(user_directory):
            os.chdir(user_directory)
            files = os.listdir()
            return Response(str(files), mimetype='text/plain')
    return Response('Invalid username or directory not found.', status=400)

if __name__ == '__main__':
    # Run app without debug mode (CWE-94 and CWE-215)
    app.run(debug=False)