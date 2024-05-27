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
    if 'file' not in request.files:
        return 'No file part in the request'
    file = request.files['file']
    filename = secure_filename(file.filename)
    
    if filename == '':
        return 'No selected file'
        
    if os.path.exists(filename):
        os.remove(filename)
        return 'File deleted successfully'
    else:
        return 'File not found'
        
if __name__ == '__main__':
    app.run()