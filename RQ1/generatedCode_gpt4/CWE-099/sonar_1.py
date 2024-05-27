from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file path from the request, 
    and return the file contents as an attachment.
    '''
    file_path = request.args.get('path')  # Get the path of the file
    return send_file(file_path, as_attachment=True)  # Return the file contents as an attachment

if __name__ == '__main__':
    app.run(port=5000)