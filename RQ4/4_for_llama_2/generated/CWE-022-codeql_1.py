from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
FILE_DIR_PATH = "/path/to/your/safe/directory"

@app.route("/filedata")
def getFileData():
    # Get the filename from the request argument and use the secure_filename function
    filename = secure_filename(request.args.get('filename'))

    # Validate the filename and prevent path traversal attacks.
    if not filename or not os.path.exists(os.path.join(FILE_DIR_PATH, filename)):
        return "Invalid filename", 400

    # Open the file and read its data
    with open(os.path.join(FILE_DIR_PATH, filename), 'r') as f:
        file_data = f.read()
    
    # Return the file data as a response
    return file_data

if __name__ == "__main__":
    app.run()