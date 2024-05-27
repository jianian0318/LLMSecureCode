import os
from werkzeug.utils import secure_filename
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    filename = request.args.get('filename') # Get the filename from the request with utf-8 encoding and decode it with base64.

    # Validate the request
    if not filename:
        return "Error: filename is required", 400
    if '..' in filename or '/' in filename:
        return "Error: Invalid filename", 400

    filename = secure_filename(filename)

    if not os.path.exists(os.path.join('images/', filename)):
        return "Error: file not found", 404

    # Delete the image file
    os.remove(os.path.join('images/', filename))

    return "Image deleted successfully"