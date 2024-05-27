from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    file_path = request.args.get('file_path')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
