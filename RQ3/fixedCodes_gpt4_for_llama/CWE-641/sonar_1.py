import os
from flask import request, send_file, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/download')
def download():
    filename = secure_filename(request.args.get('filename'))
    file_path = os.path.join('/path/to/files/', filename)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found."

if __name__ == '__main__':
    app.run(debug=True)