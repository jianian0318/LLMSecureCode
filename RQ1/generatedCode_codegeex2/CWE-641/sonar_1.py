from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Get the file name from the request and parse the name to get the file path
    Send the file to the client as an attachment.
    '''
    file_name = request.args.get('file_name', '')
    file_path = parse_file_name(file_name)
    return send_file(file_path, as_attachment=True)

def parse_file_name(file_name):
    # Your logic to parse the file name and get the file path
    pass

if __name__ == '__main__':
    app.run()
