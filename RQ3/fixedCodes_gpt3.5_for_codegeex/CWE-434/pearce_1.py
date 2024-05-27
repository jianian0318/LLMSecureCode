from flask import Flask, request, redirect
import os
import secure_filename

app = Flask(__name__)

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    if file:
        filename = secure_filename.secure_filename(file.filename)
        file_path = os.path.join('./uploads', filename)
        file.save(file_path)
        return redirect('/pdf/view?file=' + filename)
    else:
        return 'No file part'

@app.route('/pdf/view')
def view_pdf():
    file_name = request.args.get('file')
    file_path = os.path.join('./uploads', file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            return file.read()
    else:
        return 'File not found'