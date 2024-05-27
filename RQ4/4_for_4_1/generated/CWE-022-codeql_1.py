from flask import Flask, request, jsonify, abort
import os

app = Flask(__name__)

@app.route("/filedata", methods=['GET'])
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    try:
        filename = request.args.get('filename', default=None, type=str)
        
        if filename is None:
            return jsonify({"Error": "Missing filename parameter."}), 400

        if not os.path.isfile(filename):
            return jsonify({"Error": "File doesn't exist."}), 404

        with open(filename, "r") as file:
            file_data = file.read()

        return jsonify({"data": file_data}), 200

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__ == "__main__":
    DEBUG_MODE = os.environ.get('FLASK_DEBUG', False)
    app.run(debug=DEBUG_MODE)