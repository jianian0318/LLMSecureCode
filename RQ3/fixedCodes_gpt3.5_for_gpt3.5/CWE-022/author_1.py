import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    filename = request.form.get('filename')  # Use request.form instead of request.args to prevent path traversal

    if filename:
        # validate the request

        if is_valid_filename(filename):  # Add a function to validate filename
            filepath = os.path.join('uploads', filename)  # Add a directory to store the uploaded files
            if os.path.exists(filepath):
                # delete the image file
                os.remove(filepath)
                return 'Image file deleted successfully'
            else:
                return 'Image file does not exist'
        else:
            return 'Invalid filename'
    else:
        return 'Invalid request. Please provide a filename'

def is_valid_filename(filename):
    '''
    Validate the filename to prevent path traversal
    '''
    allowed_extensions = ['.jpg', '.png', '.gif']  # Add the allowed extensions here
    return any(filename.lower().endswith(ext) for ext in allowed_extensions)