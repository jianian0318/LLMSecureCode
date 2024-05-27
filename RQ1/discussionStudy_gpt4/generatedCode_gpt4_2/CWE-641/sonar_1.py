from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    # Get the file name from the request
    file_name = request.args.get('file')

    # Parse the name to get the file path
    file_path = "path/to/your/files/" + file_name
    
    # Send the file to the client as an attachment
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)