from flask import Flask, request
import os

app = Flask(__name__)

# Define here a list of valid files that should be read
VALID_FILES = {
    "file1.txt", 
    "file2.txt",
    # Add more valid files / paths here
}

@app.route("/filedata")
def getFileData():
    # Get the filename from the request argument
    filename = request.args.get('filename')
    
    # Validate the filename
    if not filename or filename not in VALID_FILES:
        return "Invalid filename", 400
    
    # Access only files within the directory
    filename_full_path = os.path.join(os.getcwd(), filename)

    # Check file exists
    if not os.path.exists(filename_full_path):
        return "File does not exist", 404

    # Open the file and read its contents
    with open(filename_full_path, 'r') as file:
        data = file.read()

    # Return the file data as a response
    return data

if __name__ == "__main__":
    app.run()