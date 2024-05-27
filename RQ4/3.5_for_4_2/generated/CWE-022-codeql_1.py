from flask import Flask, request, jsonify
import os
import urllib.parse

app = Flask(__name__)

@app.route("/filedata", methods=['GET'])
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    # Get the filename from the request argument
    filename = request.args.get('filename')

    # Check if filename is provided and is valid
    if filename:
        # Decode the filename from URL encoding
        filename = urllib.parse.unquote(filename)

        # Sanitize the filename
        filename = os.path.basename(filename)

        # Check if the file exists in a whitelist directory
        whitelist_dir = os.path.join(app.static_folder, 'files')  # Whitelist directory
        file_path = os.path.abspath(os.path.join(whitelist_dir, filename))

        if not file_path.startswith(os.path.abspath(whitelist_dir)):
            return jsonify({"error": "Invalid filename!"})

        # Check if the file exists
        if os.path.isfile(file_path):
            # Open the file and read the data
            with open(file_path, 'r') as file:
                data = file.read()
            # Return the data of the file
            return jsonify({"data": data})
        else:
            return jsonify({"error": "File does not exist!"})
    else:
        return jsonify({"error": "Filename not provided!"})

if __name__ == "__main__":
    app.run()