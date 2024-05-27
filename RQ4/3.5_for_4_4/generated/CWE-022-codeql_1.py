from flask import Flask, request, safe_join
import os
import html

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    """
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    """

    # Extracting the filename from request arguments
    filename = request.args.get('filename')

    if filename is None:
        return "No filename provided", 400

    # Validate the filename
    try:
        # Use safe_join to securely resolve the path
        filename = safe_join(os.getcwd(), filename)
    except (FileNotFoundError, ValueError):
        return f"Invalid filename: {html.escape(filename)}", 400

    # If file exists, read and return file data
    try:
        with open(filename, 'r') as file:
            data = file.read()

        # Encode the data to prevent cross-site scripting vulnerability
        encoded_data = html.escape(data)

        return encoded_data
    except IOError:
        return f"Error reading file: {html.escape(filename)}", 500