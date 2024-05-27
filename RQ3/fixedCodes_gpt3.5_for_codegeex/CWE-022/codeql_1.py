import os
from flask import Flask, request

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
    if not os.path.isabs(filename): # Ensure that the filename is an absolute path to avoid path traversal vulnerability
        return "Error: invalid filename", 400
    if not os.path.isfile(filename): # If the file does not exist, return an error message and a 404 status code
        return "Error: file not found", 404
    
    with open(filename, 'r') as file: # Open the file in read mode
        data = file.read() # Read the file contents
        
    return data, 200 # Return the file contents with a 200 status code