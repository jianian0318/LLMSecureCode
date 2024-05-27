from flask import request, send_file, Flask
import os

app = Flask(__name__)

@app.route('/download')
def download():
    file_name = request.args.get('file_name')
    file_path = os.path.join('path/to/downloads', file_name)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()