from flask import Flask, request
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename') # Get the filename from the request argument
    
    if validateFilename(filename): # Validate the filename
        try:
            with open(filename, 'r') as file:
                data = file.read() # Read the data of the file
            return data
        except FileNotFoundError:
            return "File not found"
    else:
        return "Invalid filename"

def validateFilename(filename):
    '''
    Check if the filename is valid.
    The filename is valid if it exists and ends with ".txt".
    Returns True if valid, False otherwise.
    '''
    if filename and filename.endswith('.txt'): # Check if the filename exists and ends with ".txt"
        return True
    else:
        return False

if __name__ == "__main__":
    app.run()