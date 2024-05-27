import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    # Get the file name from the request
    file_name = secure_filename(request.args.get('file_name'))
    if not file_name:
        return "Invalid request", 400

    # Allowed directory for operation - set this to the appropriate directory
    allowed_directory = '/path/to/images'

    # Full path to the file
    full_file_path = os.path.join(allowed_directory, file_name)

    # Normalize the path to ensure it's under allowed_directory
    full_file_path = os.path.normpath(full_file_path)

    if not full_file_path.startswith(os.path.abspath(allowed_directory)):
        # Path traversal attempt detected - deny access
        return "Invalid request", 403

    # Check if the file exists
    if not os.path.exists(full_file_path):
        return "File does not exist", 404

    # Delete the image file
    try:
        os.remove(full_file_path)
        return "Image deleted successfully"
    except Exception as e:
        # Log the specific error for the developers
        logging.exception("Failed to delete image")
        # Return a generic message to the users
        return "An error occurred while deleting the image", 500

if __name__ == '__main__':
    app.run()