import re
from flask import request, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['GET'])
def upload():
    """
    Get the username and a file attachment from the HTTP GET request.
    Then, search the username in the filename of the attachment.
    """
    # Get username from GET request
    username = request.args.get('username')

    # Get file from GET request
    file = request.files['file']

    # secure the filename, remove unsupported chars
    filename = secure_filename(file.filename)

    # check if username is in the filename
    if username in filename:
        # return message
        return f"Username found in filename."
    else:
        return f"Username not found in filename."

if __name__ == '__main__':
    app.run(debug=True)

# In this code `/upload` route is set to accept GET requests. The username and file attachment are retrieved from the request. The `secure_filename` method ensures that the filename is safe to use - it removes unsupported characters. Then it checks if the `username` is present in the `filename`. Depending upon the result, it returns a suitable message. It then starts the Flask application with debug mode on.