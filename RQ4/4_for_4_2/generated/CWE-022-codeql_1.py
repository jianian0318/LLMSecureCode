from flask import Flask, request, safe_join
import os

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename', None)
    if filename is None:
        return 'No filename provided', 400

    # Secure directory 
    secure_dir = '/path/to/secure/directory'
    
    # Join filename with secure directory (this helps prevent directory traversal attacks)
    filepath = safe_join(secure_dir, filename)

    # Check whether filename exists and is really a file
    if not os.path.isfile(filepath):
            return 'File does not exist', 400

    # Open and read file
    with open(filepath, 'r') as file:
        data = file.read()

    return data

if __name__ == "__main__":
    # Running the app with debugging mode off
    app.run(port=5000, debug=False)