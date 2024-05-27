from flask import request, send_file, Flask, abort, safe_join

app = Flask(__name__)

@app.route('/download')
def download():
    filename = request.args.get('filename')
    file_path = safe_join('/path/to/files/', filename)
    
    if file_path is None:
        abort(404)
    
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)