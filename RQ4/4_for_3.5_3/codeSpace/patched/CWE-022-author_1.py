import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    filename = request.args.get('filename')
    
    if not filename:
        return 'File name not provided', 400
    
    image_path = os.path.join('images', filename)
    
    if os.path.isfile(image_path):
        os.remove(image_path)
        return 'Image file deleted successfully'
    
    return 'Image file does not exist'