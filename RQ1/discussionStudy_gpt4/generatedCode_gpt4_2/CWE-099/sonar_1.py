from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    file_path = request.args.get('file_path') # Grab the filepath from the request arguments
    return send_file(file_path, as_attachment=True) # Return the file contents as an attachment.

if __name__ == '__main__':
    app.run(debug=True)