from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/filedata", methods=['GET'])
def getFileData():
    filename = request.args.get('filename')

    if filename is not None:  
        # Remove path traversal
        filename = os.path.normpath('/' + filename).lstrip('/')

        base_dir = os.path.realpath(os.getcwd())
        abs_path = os.path.realpath(os.path.join(base_dir, filename))
        
        # Validate the filename and directory
        if os.path.commonprefix([base_dir, abs_path]) != base_dir:
            return "Invalid request."
        
        # Read the data from the file
        try:
            with open(abs_path, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            return "File not found."
        except IsADirectoryError:
            return "File not found."

        return data
    else:
        return "Invalid request."

if __name__ == "__main__":
    app.run(debug=True)