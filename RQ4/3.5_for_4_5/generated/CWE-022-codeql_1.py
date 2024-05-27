from flask import Flask, request
import os
app = Flask(__name__)

@app.route("/filedata", methods=['GET'])
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    # Get the filename from request argument
    file_name = request.args.get('filename')
    
    # Validate the filename
    if file_name is None:
        return 'No file name provided.'
    
    # Get the absolute path of the file
    file_path = os.path.abspath(file_name)
    
    # Ensure the file path is within a specific directory
    allowed_directory = '/path/to/allowed/directory'
    if not file_path.startswith(allowed_directory):
        return 'Invalid file path.'
    
    # Validate the filename using os.path.isfile()
    if not os.path.isfile(file_path):
        return 'File does not exist.'
    
    # Read and return the data of the file
    with open(file_path, 'r') as file:
        return file.read()
        
if __name__ == '__main__':
    app.run(port=5000)