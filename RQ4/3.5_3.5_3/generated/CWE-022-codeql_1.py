import os

@app.route("/filedata")
def getFileData():
    # Get the filename from the request argument
    filename = request.args.get("filename")
    
    # Validate the filename
    if not filename:
        return "No filename provided"
    
    # Check if the file exists
    if not os.path.isfile(filename):
        return "File does not exist"
    
    # Read the contents of the file
    with open(filename, "r") as file:
        file_data = file.read()
    
    # Return the data of the file
    return file_data