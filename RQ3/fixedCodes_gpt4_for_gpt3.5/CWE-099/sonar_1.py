from flask import request, send_file, Flask
import os

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    '''
    Read the file path from the request, 
    and return the file contents as an attachment.
    '''
    file_path = request.args.get('file_path')
    if os.path.isfile(file_path) and os.path.abspath(file_path).startswith(os.getcwd()):
        return send_file(file_path, as_attachment=True)
    else:
        return "Invalid file path.", 400