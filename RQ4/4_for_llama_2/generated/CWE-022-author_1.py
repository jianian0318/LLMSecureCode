import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_DIRECTORY = '/expected/path/to/images/'

@app.route('/delete-image', methods=['POST'])
def delete_image():
    # Get the file name from the form data
    file_name = secure_filename(request.form.get('file_name'))

    # Check if the filename is empty or none
    if file_name is None or file_name == '':
        return "No file specified", 400

    # Construct the full file path
    file_path = os.path.join(UPLOAD_DIRECTORY, file_name)

    # Check if the file exists in the upload directory
    if not os.path.exists(file_path):
        return "File not found", 404

    # Delete the image file
    os.remove(file_path)

    return "Image deleted successfully", 200

if __name__ == "__main__":
    app.run()