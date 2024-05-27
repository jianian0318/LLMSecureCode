from flask import Flask, request
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename')  # Get the filename from the request argument
    if filename is None:
        return "Please provide a filename"  # Return an error message if filename is not provided

    # Perform any necessary validation on the filename
    # ...

    try:
        # Read the data from the file
        with open(filename, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "File not found"  # Return an error message if the file does not exist

if __name__ == '__main__':
    app.run()