import os
from flask import Flask, request, safe_join, abort

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
        file_path = safe_join(app.root_path, file_name)
        if not file_path.startswith(app.root_path):
            abort(403)
        os.remove(file_path)
    except FileNotFoundError:
        return "File not found", 404
    return "File deleted successfully"

if __name__ == '__main__':
    app.run()