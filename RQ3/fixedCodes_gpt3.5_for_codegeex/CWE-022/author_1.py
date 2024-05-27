import os
from flask import Flask, request
from urllib.parse import unquote, unquote_plus
import base64

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    filename = request.args.get('filename') # Get the filename from the request

    # Validate the request
    if not filename:
        return "Error: filename is required", 400

    original_filename = base64.b64decode(unquote_plus(filename)).decode('utf-8')

    # Validate the filename
    if '/' in original_filename or '\\' in original_filename:
        return "Error: invalid filename", 400

    # Delete the image file
    try:
        os.remove(original_filename)
    except OSError:
        return "Error: file not found", 404

    return "Image deleted successfully"