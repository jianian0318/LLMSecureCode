from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file path from the request,
    and return the file contents as an attachment.
    '''
    file_path = request.args.get('file_path')
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return send_file(file_data, attachment_filename='downloaded_file')