import os
from flask import Flask, request

app = Flask(__name__)

def secure_filename(filename):
    """
    Ensure the filename is safe and doesn't contain any directory traversal character.
    """
    return os.path.basename(filename)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file.
    '''
    filename = request.args.get('file_name')  # Get file name from request arguments
    if filename:  # Check if file name is provided
        filename = secure_filename(filename)  # Sanitize the filename
        file_path = os.path.join('images', filename)  # Construct file path safely
        if os.path.exists(file_path):  # Check if file exists
            os.remove(file_path)  # Delete the file
            return 'Image deleted successfully'
        else:
            return 'Image does not exist'
    else:
        return 'File name is missing'

if __name__ == '__main__':
    app.run(debug=True)