import os
from flask import Flask, request, send_file
app = Flask(__name__)

@app.route("/filedata", methods=["GET"])
def getFileData():
    # Get the filename from the request argument
    filename = request.args.get("filename")

    # Validate the filename
    if filename == None:
        return "Filename not provided", 400
    if not os.path.exists(filename):
        return "File not found", 404

    # Return the data of the file
    return send_file(filename, as_attachment=True) 

if __name__ == "__main__":
    app.run(debug=True)