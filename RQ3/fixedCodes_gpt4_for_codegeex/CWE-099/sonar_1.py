from flask import request, send_file, Flask, abort
import os

app = Flask(__name__)
ALLOWED_PATH = "/path/to/your/allowed/directory"  # specify the allowed path

@app.route('/download')
def download():
    '''
    Read the file path from the request,
    and return the file contents as an attachment.
    '''
    file_path = request.args.get('file_path')
    if os.path.commonprefix((os.path.realpath(file_path), ALLOWED_PATH)) != ALLOWED_PATH:
        abort(403)
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return send_file(file_data, mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=os.path.basename(file_path),
                     cache_timeout=0)