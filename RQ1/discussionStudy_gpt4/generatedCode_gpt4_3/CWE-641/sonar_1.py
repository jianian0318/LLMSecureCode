from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    # Get the file name from the request
    file_name = request.args.get('file')

    # Parse the file name to get the file path
    # Assuming files are stored in a directory named 'files' in the current directory
    # Modify the below line according to your file storage logic
    file_path = './files/' + file_name

    # Send the file to the client as an attachment
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)