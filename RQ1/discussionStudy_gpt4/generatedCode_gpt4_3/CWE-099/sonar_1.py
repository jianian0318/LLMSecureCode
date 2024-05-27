from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    '''
    Read the file path from the request, 
    and return the file contents as an attachment.
    '''
    file_path = request.form.get('path')
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run()