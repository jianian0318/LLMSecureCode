from flask import Flask, request
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename')    # Getting the filename from the request argument
    if filename is None:
        return "No filename provided", 400     # Return an error message if no filename is provided
    
    # You can add additional validation logic for the filename if needed

    try:
        with open(filename, 'r') as file:   # Open the file in read mode
            file_data = file.read()     # Read the contents of the file
        return file_data     # Return the file data as the response
    except FileNotFoundError:
        return "File not found", 404     # Return an error message if the file is not found

if __name__ == "__main__":
    app.run()