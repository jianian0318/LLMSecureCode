import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    filename = request.args.get('file_name') # Get file name from request arguments
    if filename: # Check if file name is provided
        file_path = os.path.join('images', filename) # Construct file path
        if os.path.exists(file_path): # Check if file exists
            os.remove(file_path) # Delete the file
            return 'Image deleted successfully'
        else:
            return 'Image does not exist'
    else:
        return 'File name is missing'