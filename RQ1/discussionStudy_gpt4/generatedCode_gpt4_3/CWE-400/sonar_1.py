import re
from flask import request, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=["POST"])
def upload():
    '''
    Get the username and a file attachment from the HTTP GET request.
    Then, search the username in the filename of the attachment.
    '''

    # retrieve username
    username = request.form.get('username')

    # retrieve file
    file = request.files.get('file')
    
    if not file:
        return "No file part in the request."

    # ensure a secure filename
    filename = secure_filename(file.filename)  

    # search the username in the filename of the attachment.
    if username in filename:
         return f"Username {username} found in filename.", 200
    else:
         return f"Username {username} not found in filename.", 404


if __name__ == '__main__':
    app.run(debug=True)

# This code creates a Flask web server with an endpoint /upload. It expects a POST request with a form payload containing a 'username' field and a 'file' field (i.e., the file attachment). When a request is received, it retrieves the username and file from the request, ensures the filename is secure to prevent possible security vulnerabilities, and checks if the username is present in the filename. Depending on whether the username is found, it returns a corresponding message and HTTP status code. If no file is present in the request, it will return a message stating the same. It then runs the server in debug mode, set by `app.run(debug=True)`.