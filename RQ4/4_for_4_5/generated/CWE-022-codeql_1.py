from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    
    # Get the filename from request arguments
    filename = request.args.get('name', default = None, type = str)
    
    # Check if filename provided
    if filename is None:
        return "No file name provided", 400
    
    # Check if file exists
    if not os.path.isfile(filename):
        return "File does not exist", 400
    
    # Return the file data
    with open(filename, 'r') as file:
        file_data = file.read()
    return file_data


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)