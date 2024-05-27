from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    filename = request.args.get('filename')
    file_path = f'/path/to/files/{filename}'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
