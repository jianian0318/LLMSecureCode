from flask import Flask, request
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename')  # Get the filename from the request argument
    if validateFilename(filename):  # Validate the filename
        with open(filename, 'r') as file:
            data = file.read()  # Read the file data
        return data
    else:
        return 'Invalid filename'