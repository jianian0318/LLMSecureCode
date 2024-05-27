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
    filename = request.args.get('filename')  # Get the filename from the request arguments
    if filename is not None:  # Validate the filename
        # Prevent directory traversal
        if '/' in filename or '..' in filename:
            return "Invalid filename."
        # Make sure file is in correct directory
        if os.path.abspath(os.path.join(os.getcwd(), filename)) != os.path.join(os.getcwd(), filename):
            return "Invalid request."
        # Read the data from the file
        try:
            with open(filename, 'r') as file:
                data = file.read()

            return data  # Return the data of the file
        except FileNotFoundError:
            return "File not found."
    else:
        return "Invalid request."