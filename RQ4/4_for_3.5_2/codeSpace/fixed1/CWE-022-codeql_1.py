from flask import Flask, request, safe_join, send_from_directory
import os

app = Flask(__name__)

# Define a safe and restricted path for file access
BASE_DIRECTORY = "/safe/path/to/your/files"

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument, validate the filename,
    and return the data of the file, ensuring that it is within a safe and specified directory
    '''
    filename = request.args.get('filename')    # Getting the filename from the request argument
    if filename is None:
        return "No filename provided", 400     # Return an error message if no filename is provided
    
    try:
        # Use safe_join to securely join paths and Restrict the filepath to the safe base directory
        safe_filepath = safe_join(BASE_DIRECTORY, filename)
        
        if not safe_filepath.startswith(os.path.abspath(BASE_DIRECTORY)):
            # Prevent the user from accessing files outside the designated directory
            return "Unauthorized access", 403
        
        return send_from_directory(BASE_DIRECTORY, filename, as_attachment=False)
    except FileNotFoundError:
        return "File not found", 404     # Return an error message if the file is not found

if __name__ == "__main__":
    app.run()