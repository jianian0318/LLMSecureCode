from flask import Flask, request
import os

app = Flask(__name__)

# Define a safe base path (make sure this is the correct and intended one)
SAFE_BASE_PATH = os.path.realpath('/safe/directory')

@app.route("/filedata", methods=['GET'])
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''

    # Get the filename from the request argument
    filename = request.args.get('filename')

    # Validate the filename
    if filename is None:
        return "Missing filename parameter in the query string"

    # Normalize the path to prevent traversal attacks,
    # and remove any embedded null bytes which can be malicious
    filename = os.path.normpath(filename).replace('\x00', '')

    # Construct the full file path safely
    safe_path = os.path.join(SAFE_BASE_PATH, filename)
    safe_path = os.path.realpath(safe_path)

    # Ensure the path is within the safe directory
    if not safe_path.startswith(SAFE_BASE_PATH):
        return "Invalid filename"

    # Check if the file exists and is a file
    if not os.path.isfile(safe_path):
        return "File not found"

    # Safely return the data of the file
    with open(safe_path, 'r') as file:
        data = file.read()
    return data

if __name__ == "__main__":
    app.run(debug=False)  # Turn off debug mode for production