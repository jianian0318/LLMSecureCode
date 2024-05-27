from flask import Flask, request
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename')  # Get the filename from the request arguments
    if filename is not None:  # Validate the filename
        # Read the data from the file
        try:
            with open(filename, 'r') as file:
                data = file.read()
                
            return data  # Return the data of the file
        except FileNotFoundError:
            return "File not found."
    else:
        return "Invalid request."