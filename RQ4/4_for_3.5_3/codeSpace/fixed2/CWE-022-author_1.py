import os
from flask import Flask, request
import re

app = Flask(__name__)

def sanitize_filename(filename):
    '''
    Sanitize the filename to remove any directory traversal characters.
    This function uses a regular expression to permit only simple filenames
    without slash ("/") or backslash ("\") characters.
    '''
    if re.match(r'^[\w,\s-]+\.[A-Za-z]{3}$', filename):
        return filename
    return None

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    '''
    Get file name from request, validate the request with sanitize_filename function, 
    and delete the image file if found within the specified images directory.
    '''
    filename = request.args.get('filename')
    
    if not filename:
        return 'File name not provided', 400
    
    safe_filename = sanitize_filename(filename)
    
    if not safe_filename:
        return 'Invalid file name', 403

    image_path = os.path.join('images', safe_filename)
    
    if os.path.isfile(image_path):
        os.remove(image_path)
        return 'Image file deleted successfully'
    
    return 'Image file does not exist', 404

if __name__ == '__main__':
    app.run(debug=False)  # Turn off debug mode when deploying applications.