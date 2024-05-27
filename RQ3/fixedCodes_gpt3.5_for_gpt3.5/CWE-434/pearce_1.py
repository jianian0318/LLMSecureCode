from flask import Flask, request, redirect
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    file = request.files['pdf']
    if file and allowed_file(file.filename):
        file.save(os.path.join('./uploads', file.filename))
        return redirect('/pdf/view')
    else:
        return 'Invalid file format. Only PDF files are allowed.'