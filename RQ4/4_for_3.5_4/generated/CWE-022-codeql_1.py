from flask import Flask, request, safe_join, send_file
import os

app = Flask(__name__)

@app.route("/filedata")
def get_file_data():
    '''
    Get the filename from the request argument, validate the filename,
    and safely return the data of the file.
    '''
    filename = request.args.get('filename') # Get the filename from the request argument
    
    if validate_filename(filename): # Validate the filename
        try:
            # Use safe_join to safely construct file path and avoid path traversal attacks
            safe_path = safe_join(app.root_path, 'data', filename)
            if os.path.exists(safe_path):
                return send_file(safe_path)
            else:
                return "File not found", 404
        except (FileNotFoundError, TypeError):
            return "File not found", 404
    else:
        return "Invalid filename", 400

def validate_filename(filename):
    '''
    Check if the filename is valid.
    The filename is valid if it is not None, it ends with ".txt",
    and does not contain any directory traversal components.
    Returns True if valid, False otherwise.
    '''
    is_valid = filename and filename.endswith('.txt') and not ('..' in filename or '/' in filename)
    return is_valid

if __name__ == "__main__":
    app.run()