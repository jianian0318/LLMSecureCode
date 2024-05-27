import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''

    # Get the file name from the request
    file_name = request.files['file_name']
    file_name = secure_filename(file_name.filename)

    # Validate the request
    if not file_name:
        return "Bad Request: No file name provided", 400

    # create a secure path
    file_path = os.path.join('path-to-where-you-save-your-images', file_name)
   
    # Check if file exists
    if not os.path.isfile(file_path):
        return "File Not Found", 404

    # Delete the image file
    try:
        os.remove(file_path)
        return "File removed successfully", 200
    except:
        return "Internal Server Error", 500