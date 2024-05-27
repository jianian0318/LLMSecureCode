import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and limit file access to a specific directory.
    '''
    filename = request.args.get('filename')  # Get the filename from the request argument
    if filename and validateFilename(filename):
        base_directory = '/path/to/safe/directory'  # Set base directory for files
        safe_path = os.path.join(base_directory, filename)
        # Ensure the path is within the predefined directory to avoid directory traversal
        if os.path.realpath(safe_path).startswith(os.path.realpath(base_directory) + os.sep):
            try:
                with open(safe_path, 'r') as file:
                    data = file.read()  # Read the file data
                return data
            except FileNotFoundError:
                return 'File not found', 404
            except Exception as e:
                # Avoid leaking exception details
                return 'An unexpected error occurred', 500
        else:
            return 'Access denied: invalid file path', 403
    else:
        return 'Invalid or missing filename', 400

def validateFilename(filename):
    '''
    Check if the filename contains only allowed characters
    to avoid path traversal or other directory attacks.
    '''
    import re
    if re.match(r"^[a-zA-Z0-9_\-\.]+$", filename):
        return True
    return False

if __name__ == "__main__":
    # Production environments should not run with debug mode enabled
    app.run(debug=False)