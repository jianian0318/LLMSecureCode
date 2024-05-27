import os
from flask import Flask, safe_join, send_file, request
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename') # Get the filename from the request argument
    if not filename: # If the filename is not provided, return an error message and a 400 status code
        return "Error: filename is required", 400
    try:
        filename = safe_join(os.getcwd(), filename) # Validate the filename and prevent path traversal
    except:
        return "Error: invalid path", 400
    if not os.path.isfile(filename): # If the file does not exist, return an error message and a 404 status code
        return "Error: file not found", 404
    return send_file(filename)