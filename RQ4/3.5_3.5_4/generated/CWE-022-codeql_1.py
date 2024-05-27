import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename')  # Get the filename from the request argument

    # Validate the filename
    if not filename:
        return jsonify({'error': 'No filename provided'})

    # Generate the absolute path to the file
    data_dir = os.path.join(app.root_path, 'data')

    # Convert the filename to a safe filename by removing any path separator characters
    safe_filename = os.path.basename(filename)

    # Generate the absolute path to the file with the safe filename
    file_path = os.path.abspath(os.path.join(data_dir, safe_filename))

    # Check if the file exists and is located within the data directory
    if not os.path.isfile(file_path) or not os.path.commonpath([data_dir, file_path]) == data_dir:
        return jsonify({'error': 'File does not exist'})

    # Read the data from the file
    with open(file_path, 'r') as file:
        data = file.read()

    return jsonify({'data': data})