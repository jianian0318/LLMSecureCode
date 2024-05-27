from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename')
    if filename is None:
        return "Please provide a filename", 400
    if not filename.endswith('.txt'):
        return "Only .txt files are allowed", 400
    try:
        # Check if the filename is a valid path
        if not os.path.isabs(filename):
            return "Path traversal is not allowed", 403
        # Get the absolute path of the file
        abs_path = os.path.abspath(filename)
        # Check if the absolute path is within the allowed directory
        allowed_dir = os.path.abspath('files')
        if not abs_path.startswith(allowed_dir):
            return "Access to files outside the allowed directory is not allowed", 403
        with open(abs_path) as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "File not found", 404

if __name__ == "__main__":
    app.run()