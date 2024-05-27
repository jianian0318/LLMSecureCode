from flask import Flask, request, send_file, abort
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate that the filename is safe to use,
    and return the data of the file.
    '''
    filename = request.args.get('filename', None)

    if filename is None:
        abort(400, 'filename is not provided')

    filename = secure_filename(filename)  # secure_filename ensures that the filename is safe to use

    file_path = os.path.join('static', filename)  # Path should be adjusted based on your configuration

    if os.path.isfile(file_path):
        return send_file(file_path)
    else:
        abort(404, "File not found")

if __name__ == "__main__":
    app.run(debug=False)  # Do not run Flask in debug mode in a production setting