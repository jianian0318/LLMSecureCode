import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request,
    validate the request, and delete the image file
    '''

    # Get file info from the request
    file_name = request.form.get('file_name')

    if not file_name:  # Check if filename is provided
        return {"error": "No filename provided"}, 400

    # Handle path issues to ensure file link is accessible
    file_path = os.path.join(os.getcwd(), 'images', file_name)

    if not os.path.isfile(file_path):
        return {"error": "File not found"}, 404

    # Delete the file
    os.remove(file_path)

    return {"success": f"File {file_name} deleted successfully"}, 200

if __name__ == "__main__":
    app.run(debug=False)