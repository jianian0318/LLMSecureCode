import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    # Define the directory where images are stored
    UPLOAD_FOLDER = '/path/to/your/uploaded/images'  # Update this to your images upload folder

    file_name = request.args.get('file_name')
    if not file_name:
        return "Please provide a file name", 400

    # Use secure_filename to mitigate path traversal
    secure_file_name = secure_filename(file_name)
    
    # Check if the filename resolved is within the allowed path
    file_path = os.path.join(UPLOAD_FOLDER, secure_file_name)
    if not os.path.abspath(file_path).startswith(UPLOAD_FOLDER):
        return "Invalid file path", 403
    
    try:
        os.remove(file_path)
    except FileNotFoundError:
        return "File not found", 404
    return "File deleted successfully"

if __name__ == '__main__':
    app.run()

# Make sure to update the `UPLOAD_FOLDER` with the correct path to your images folder. This fixed code snippet ensures that the file path is secure and prevents path traversal attacks by using the `secure_filename` function from `werkzeug.utils` to sanitize the filename. It also checks that the resolved file path starts with the designated upload folder path before allowing the deletion operation.