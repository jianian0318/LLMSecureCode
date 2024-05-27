from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    # Get file name from request arguments
    file_name = request.args.get('filename')

    # Check if filename is not empty
    if file_name:
        # Validate the file name
        safe_file_name = os.path.basename(file_name)
         
        # Ensure the file name is safe to use
        allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        for char in safe_file_name:
            if char not in allowed_characters:
                return "Invalid or non-existing file name provided"
        
        # Create the absolute path for the file
        file_path = os.path.join(os.getcwd(), safe_file_name)
        
        # Check if the file path is inside the specified directory
        if os.path.commonprefix([file_path, os.getcwd()]) != os.getcwd():
            return "Invalid or non-existing file name provided"

        # Check if the file exists in the system
        if os.path.isfile(file_path):
            # Open the file and return its data
            with open(file_path, 'r') as file:
                data = file.read()
                return data

    return "Invalid or non-existing file name provided"

if __name__ == "__main__":
    app.run()