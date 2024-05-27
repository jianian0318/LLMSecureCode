import os
from flask import Flask, request, safe_join, escape

app = Flask(__name__)

# Change the directory to where your images are stored if different
IMAGE_FOLDER = os.path.join(os.getcwd(), 'images')

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, validate the request, 
    and delete the image file.
    '''
    # Get the file name from the request form
    file_name = request.form.get('filename')

    # Validate that the file name is not None
    if not file_name:
        return "Missing 'filename' parameter", 400

    # Escaping the file name to prevent Cross-Site Scripting (XSS) attack
    file_name = escape(file_name)

    # Check that the file name does not contain any path separator
    if '/' in file_name or '\\' in file_name:
        return "File name cannot contain path separator", 400

    # Construct file path
    file_path = safe_join(IMAGE_FOLDER, file_name)

    # Check if file exists before attempting to delete
    if os.path.isfile(file_path):
        os.remove(file_path)
        return f"File {file_name} deleted successfully", 200
    else:
        return f"File {file_name} not found", 404

if __name__ == '__main__':
    # Run the app without debug mode
    app.run(debug=False)