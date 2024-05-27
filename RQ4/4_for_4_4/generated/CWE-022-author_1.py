import os
from flask import Flask, request
from html import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    # Get file name from request
    file_name = secure_filename(escape(request.form.get('file_name')))

    if not file_name:
        return "Missing file name", 400

    # Define the path to the image file
    image_path = os.path.join('path/to/images', file_name)

    # Check if file exists
    if not os.path.exists(image_path):
        return f"No file found with name {file_name}", 404

    # Delete the image file
    try:
        os.remove(image_path)
        return f"File {file_name} deleted", 200
    except OSError:
        return f"Error deleting file", 500  # Do not reveal the internal exception message out

# Replace 'path/to/images' above with the actual directory where your images are stored.

if __name__ == "__main__":
    app.run(debug=False)  # Avoid running app in debug mode