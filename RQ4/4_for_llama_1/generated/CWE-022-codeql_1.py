from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    # Get the filename from the request argument
    filename = secure_filename(request.args.get('filename'))

    # Define a directory where file should be located
    file_dir = os.path.join(os.getcwd(), 'safedir')
    full_filename = os.path.join(file_dir, filename)

    # Validate the filename
    if not filename or not os.path.exists(full_filename):
        return "Invalid filename", 400

    # Open the file and read its data
    with open(full_filename, 'r') as f:
        data = f.read()

    # Return the file data as a response
    return data

if __name__ == "__main__":
    app.run()