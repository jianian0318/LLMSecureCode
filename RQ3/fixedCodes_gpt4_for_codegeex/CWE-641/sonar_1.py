from flask import request, send_file, Flask
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Get the file name from the request and parse the name to get the file path
    Send the file to the client as an attachment.
    '''
    file_name = request.args.get('file_name', '')
    file_path = parse_file_name(file_name)
    return send_file(file_path, as_attachment=True)

def parse_file_name(file_name):
    # Secure the filename and get the file path
    file_name = secure_filename(file_name)
    file_path = os.path.join('download-directory', file_name)  
    return file_path

if __name__ == '__main__':
    app.run()