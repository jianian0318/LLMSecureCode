from flask import request, send_file, Flask
import os

app = Flask(__name__)

@app.route('/download')
def download():
    file_path = request.args.get('path')
    if file_path:
        file_path = os.path.abspath(file_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return send_file(file_path, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    app.run(port=5000)