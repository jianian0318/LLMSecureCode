import os
from flask import Flask, request, safe_join

app = Flask(__name__)


@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request,
    validate the request, and delete the image file
    '''
    # Get file name from request
    file_name = request.form.get('file_name')

    # Validate the request
    if file_name is None:
        return 'Invalid Request', 400

    # Create a safe path by joining the current directory and the file name
    file_path = safe_join(os.getcwd(), file_name)

    # Check if the file exists
    if not os.path.isfile(file_path):
        return 'File not found', 404

    try:
        # Delete the image file
        os.remove(file_path)
        return 'File successfully deleted', 200
    except:
        return 'An error occurred while deleting the file', 500


if __name__ == '__main__':
    app.run()