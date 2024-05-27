import os
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
    if not os.path.isfile(filename):
        return "Error: file not found", 404

    # Delete the image file
    os.remove(filename)

    return "Image deleted successfully"