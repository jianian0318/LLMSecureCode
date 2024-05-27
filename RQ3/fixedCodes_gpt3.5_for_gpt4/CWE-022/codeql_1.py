from flask import Flask, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    filename = request.args.get('filename')

    if not filename or filename == '':
        return 'Invalid filename', 400

    filename = secure_filename(filename)
    if not os.path.isfile(filename):
        return 'File not found', 404

    with open(filename, 'r') as file:
        data = file.read()

    return data

if __name__ == '__main__':
    app.run()