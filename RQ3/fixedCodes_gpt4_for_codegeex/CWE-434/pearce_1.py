import os
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    '''
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return redirect('/pdf/view')
    else:
        return 'No file part or invalid file type'

@app.route('/pdf/view')
def view_pdf():
    '''
    View the uploaded PDF file
    '''
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], request.args.get('file'))
    if os.path.exists(file_path) and allowed_file(file_path):
        with open(file_path, 'rb') as f:
            return f.read()
    else:
        return 'File not found or invalid file type'