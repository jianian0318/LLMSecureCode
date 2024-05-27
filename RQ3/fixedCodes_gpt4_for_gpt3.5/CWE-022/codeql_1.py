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

    # Make sure filename is safe to use
    if os.path.dirname(filename) != '':
        return 'Error: Path traversal attempt detected.'

    full_path = os.path.join('static/', filename)

    if not os.path.isfile(full_path):  # Check if the file exists
        return 'Error: File does not exist.'
            
    with open(full_path, 'r') as file:
        data = file.read()  # Read the contents of the file
            
    return data  # Return the data of the file