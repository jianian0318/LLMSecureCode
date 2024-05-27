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
    filename = request.args.get('filename')

    if filename:
        # validate the request
        filename = secure_filename(filename)

        if os.path.exists(filename):
            # delete the image file
            os.remove(filename)
            return 'Image file deleted successfully'
        else:
            return 'Image file does not exist'
    else:
        return 'Invalid request. Please provide a filename'