from flask import Flask, request, abort
import os
import urllib.parse

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename', '')

    # validate the filename
    if not filename:
        return "No filename provided"

    # validate the filename path
    base_path = os.path.join(os.getcwd(), 'files/') # Specify the base path where the files are stored

    # Clean the filename to prevent path traversal attacks
    clean_filename = os.path.basename(filename)
    full_path = os.path.join(base_path, clean_filename) # Join the base path and the filename

    # Check if the file path is within the base path
    if not full_path.startswith(base_path):
        return "Invalid file path"

    if not os.path.isfile(full_path):
        return "File does not exist"

    # read the file and return its data
    with open(full_path, 'r') as file:
        file_data = file.read()

    return file_data

if __name__ == "__main__":
    app.run()