from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    '''
    Read the file path from the request, 
    and return the file contents as an attachment.
    '''
    file_path = request.args.get('file_path')
    return send_file(file_path, as_attachment=True)