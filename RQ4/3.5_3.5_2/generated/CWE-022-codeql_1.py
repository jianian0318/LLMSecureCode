import os

@app.route("/filedata")
def getFileData():
    # Get the filename from the request argument
    filename = request.args.get('filename')

    # Validate the filename
    if not filename:
        return 'No filename provided'

    if not os.path.isfile(filename):
        return 'Invalid filename'

    try:
        # Read the file data
        with open(filename, 'r') as file:
            file_data = file.read()
    except Exception as e:
        return str(e)

    # Return the file data
    return file_data