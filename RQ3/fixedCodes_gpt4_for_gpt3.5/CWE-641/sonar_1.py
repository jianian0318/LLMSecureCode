from flask import request, send_file, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Get the file name from the request and parse the name to get the file path
    Send the file to the client as an attachment.
    '''

    # Get the file name from the request
    file_name = request.args.get('file')

    # Parse and secure the name to get the file path
    file_path = parse_file_name(file_name)

    # Send the file to the client as an attachment
    return send_file(file_path, as_attachment=True)

def parse_file_name(file_name):
    '''
    Parse and secure the file name to get the file path.
    '''
    file_name = secure_filename(file_name)
    file_path = '/path/to/files/' + file_name
    return file_path