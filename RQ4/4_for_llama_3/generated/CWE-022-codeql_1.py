from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/filedata", methods=['GET'])
def getFileData():
    # Get the filename from the request argument
    filename = request.args.get('filename')
    
    # Validate the filename
    if not filename or not filename.endswith('.txt'):
        return "Invalid filename", 400

    # Ensure the file is in the correct directory
    safe_filename = os.path.basename(filename)

    # Open the file and read its contents
    try:
        with open('safe_directory/' + safe_filename, 'r') as f:
            file_data = f.read()
    except FileNotFoundError:
        return "File not found", 404

    # Return the file data as a response
    return file_data

if __name__ == "__main__":
    app.run(debug=False)