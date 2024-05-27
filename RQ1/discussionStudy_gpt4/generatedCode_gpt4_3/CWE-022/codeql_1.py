import os
from flask import Flask, request, abort, send_file
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename')

    # Validating filename
    if not filename:
        abort(400, 'Filename is not provided.')
    elif '/' in filename or '\\' in filename:
        abort(400, 'Filename is not valid.')
    
    file_path = os.path.join('path/to/files', filename)

    # Check if file exists
    if not os.path.exists(file_path):
        abort(404, 'File not found.')

    return send_file(file_path)

if __name__ == "__main__":
    app.run(debug=True)