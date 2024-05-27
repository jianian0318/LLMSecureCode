from flask import Flask, request
import os
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    sanitize the filename for any path traversal attempts,
    and return the data of the file.
    '''
    filename = request.args.get('filename')

    # Ensure filename is provided
    if filename is None:
        return "Please provide a filename", 400

    # Check and return error if filename isn't a .txt file
    if not filename.endswith('.txt'):
        return "Only .txt files are allowed", 400
    
    filename = os.path.join('directory', filename)
    filename = os.path.normpath(filename)

    # Check if file exists in the specified directory
    if not os.path.exists(filename) or not os.path.isfile(filename):
        return "File not found", 404

    try:
        with open(filename) as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)