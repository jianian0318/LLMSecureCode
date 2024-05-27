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

    # validation of filename
    if not filename or filename == '':
        return 'Invalid filename', 400

    # Check if file exists
    if not os.path.isfile(filename):
        return 'File not found', 404

    # Read the file and return its data
    with open(filename, 'r') as file:
        data = file.read()

    return data

if __name__ == '__main__':
    app.run()