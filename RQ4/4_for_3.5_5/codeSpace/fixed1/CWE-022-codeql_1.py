from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename to ensure it does not access unintended files,
    and return the data of the file.
    '''
    filename = request.args.get('filename')  # Get the filename from the request argument
    if filename is None:
        return "Please provide a filename"  # Return an error message if filename is not provided

    # Prevent users from accessing files outside the designated directory
    allowed_directory = '/path/to/allowed/directory'
    
    # Normalize the requested filename to an absolute path
    safe_filename = os.path.abspath(os.path.join(allowed_directory, filename))
    
    # Check if the resolved filename is under the allowed directory
    if not safe_filename.startswith(allowed_directory):
        return "Access denied: You are not allowed to access files outside of the allowed directory."

    try:
        # Read the data from the file, ensuring it's under the allowed directory
        with open(safe_filename, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "File not found"  # Return an error message if the file does not exist

if __name__ == '__main__':
    app.run()