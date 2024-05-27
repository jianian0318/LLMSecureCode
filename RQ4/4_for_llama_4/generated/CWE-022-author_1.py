import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define directory to store images
IMAGES_DIR = '/path/to/images/dir'

@app.route('/deleteImage')
def deleteImage():
    # Get the file name from the request
    file_name = request.args.get('file_name')
    file_name = secure_filename(file_name) 

    # Get full path of the file in the secure directory
    file_path = os.path.join(IMAGES_DIR, file_name)

    # Check and delete the file
    if file_name and os.path.exists(file_path):
        os.remove(file_path)
        return "Image deleted successfully"
    else:
        return "Invalid request or file not found"

if __name__ == '__main__':
    app.run()