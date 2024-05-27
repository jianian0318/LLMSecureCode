import os
from flask import Flask, request, redirect, url_for, escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])

def deleteImage():
    '''
    Get file name from request, validate the request, and delete the image file without exposing any exception details to the users
    '''
    filename = None

    try:
        # Get the file name from the request
        filename = request.form['filename']

        # Use secure_filename function from werkzeug.utils
        # This function can prevent directory traversal attacks
        filename = secure_filename(filename)

        # Check if the file exist
        img_path = os.path.join('./images', filename)
        if not os.path.isfile(img_path):
            return "File not found", 404

        # Delete the file
        os.remove(img_path)

    except Exception as e:
        # Don't expose exception details to the user
        return "An error occurred. Please try again.", 500

    # Response message, escape output to prevent Cross-Site Scripting (XSS) attacks
    return '{} has been deleted.'.format(escape(filename)), 200

if __name__ == "__main__":
    # Don't run Flask app in debug mode in a production environment to prevent arbitrary code execution through the Werkzeug debugger
    app.run(debug=False)