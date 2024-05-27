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
    filename = request.args.get('filename')  # Retrieve the filename from the request argument
    
    if not filename:  # Check if filename is missing or empty
        return 'Error: Please provide a filename.'
    
    if not os.path.isfile(os.path.join('path/to/files', filename)):  # Check if the file exists
        return 'Error: File does not exist.'
    
    with open(os.path.join('path/to/files', filename), 'r') as file:
        data = file.read()  # Read the contents of the file
        
    return data  # Return the data of the file