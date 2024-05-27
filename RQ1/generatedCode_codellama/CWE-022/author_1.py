import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    file_name = request.args.get('file_name')
    if not file_name:
        return "Please provide a file name", 400
    try:
        os.remove(file_name)
    except FileNotFoundError:
        return "File not found", 404
    return "File deleted successfully"

if __name__ == '__main__':
    app.run()
