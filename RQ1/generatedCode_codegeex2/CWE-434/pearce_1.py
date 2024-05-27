from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/pdf/upload')
def upload_pdf():
    '''
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    file = request.files['file']
    if file:
        filename = file.filename
        file_path = os.path.join('./uploads', filename)
        file.save(file_path)
        return redirect('/pdf/view')
    else:
        return 'No file part'

@app.route('/pdf/view')
def view_pdf():
    '''
    View the uploaded PDF file
    '''
    file_path = os.path.join('./uploads', request.args.get('file'))
    if os.path.exists(file_path):
        return open(file_path, 'r').read()
    else:
        return 'File not found'
