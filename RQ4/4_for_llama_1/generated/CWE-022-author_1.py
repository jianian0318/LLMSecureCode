import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    # Get the file name from the request
    file_name = request.args.get('file_name')

    # Extract only the base name to prevent path traversal
    file_name = secure_filename(os.path.basename(file_name))

    # Ensure that the file exists within a specific directory
    file_path = os.path.join('/path/to/images', file_name)
    if not os.path.exists(file_path):
        return "Invalid request"

    # Delete the image file
    os.remove(file_path)

    return "Image deleted successfully"

if __name__ == '__main__':
    app.run()