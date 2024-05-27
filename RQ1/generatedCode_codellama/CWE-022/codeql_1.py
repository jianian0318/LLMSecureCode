from flask import Flask, request
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    filename = request.args.get('filename')
    if filename is None:
        return "Please provide a filename", 400
    if not filename.endswith('.txt'):
        return "Only .txt files are allowed", 400
    try:
        with open(filename) as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "File not found", 404

if __name__ == "__main__":
    app.run()
