from flask import Flask, request, send_file
import os
import re

# Define the allowed directory
ALLOWED_DIRECTORY = "/home/user/allowed_directory"

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    # Get the filename from the request argument
    filename = request.args.get('filename', '')

     # Verify the filename contains only allowed characters
    if not re.match('^[0-9a-zA-Z._-]+$', filename):
        return "Invalid filename", 400

    # Construct the complete path using safe join
    complete_path = safe_join(ALLOWED_DIRECTORY, filename)

    # Validate the filename
    if complete_path is None or not os.path.exists(complete_path):
        return "Invalid filename", 400

    # Open the file and read its data
    with open(complete_path, 'r') as f:
        data = f.read()

    # Return the file data as a response
    return data

# Safe join function to prevent path traversal
def safe_join(base, *paths):
    if base is None:
        base = os.getcwd()

    final_path = os.path.normpath(os.path.join(base, *paths))

    if final_path.startswith(base):
        return final_path

if __name__ == "__main__":
    app.run()