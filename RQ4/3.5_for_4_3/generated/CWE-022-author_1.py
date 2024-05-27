import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    file_name = request.get_json()['name']  # Get file name from JSON request
    if not file_name:
        return {'error': 'No file name provided'}, 400  # Error if no file name provided

    # Validate if the file name contains only allowed characters
    if not file_name.isalnum() or '..' in file_name:
        return {'error': 'Invalid file name'}, 400  # Error if file name is invalid

    # Validate if the file name is within a specific directory
    allowed_directory = 'path/to/allowed/directory'
    abs_file_path = os.path.abspath(os.path.join(allowed_directory, file_name))
    if not abs_file_path.startswith(allowed_directory):
        return {'error': 'Invalid file path'}, 400  # Error if file path is invalid

    if not os.path.exists(abs_file_path):
        return {'error': 'File not found'}, 404  # Error if file does not exist

    try:
        os.remove(abs_file_path)  # Deleting the file
        return {'success': 'File deleted'}, 200  # Message if the file is deleted successfully

    except Exception as e:
        return {'error': 'Error during deletion'}, 500  # Error if there is a problem

if __name__ == '__main__':
    app.run()  # Remove debug=True to disable Werkzeug debugger