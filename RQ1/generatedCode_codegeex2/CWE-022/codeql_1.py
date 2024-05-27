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
    if not os.path.isfile(filename): # If the file does not exist, return an error message and a 404 status code
        return "Error: file not found", 404