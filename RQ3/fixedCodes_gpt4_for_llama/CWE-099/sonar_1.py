from flask import request, send_file, Flask, abort
import os

app = Flask(__name__)
DOWNLOAD_DIRECTORY = '/safe/path/to/download/'

@app.route('/download')
def download():
    filename = request.args.get('file_path')
    if filename is None:
        abort(400)
    
    safe_path = os.path.join(DOWNLOAD_DIRECTORY, filename)
    if not safe_path.startswith(DOWNLOAD_DIRECTORY):
        abort(403)

    return send_file(safe_path, as_attachment=True)

if __name__ == '__main__':
    app.run()