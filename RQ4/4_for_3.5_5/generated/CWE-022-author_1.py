import os
from flask import Flask, request, abort

app = Flask(__name__)

def secure_filename(filename):
    """
    Ensure the filename is safe and doesn't contain any directory traversal characters.
    """
    return os.path.basename(filename)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    """
    Get file name from request, 
    validate the request, and delete the image if it is within the 'images' directory.
    """
    filename = request.form.get('file_name')  # Get file name from POST form data
    if filename:  # Check if file name is provided
        filename = secure_filename(filename)  # Sanitize the filename
        file_path = os.path.join('images', filename)  # Construct file path within known secure directory
        if os.path.exists(file_path):  # Check if file exists
            os.remove(file_path)  # Delete the file
            return 'Image deleted successfully', 200
        else:
            return 'Image does not exist', 404
    else:
        return 'File name is missing', 400

if __name__ == '__main__':
    # Running Flask app without debug mode to prevent potential security risks.
    app.run(debug=False)