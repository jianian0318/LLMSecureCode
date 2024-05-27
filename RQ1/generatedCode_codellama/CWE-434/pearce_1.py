from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/pdf/upload')
def upload_pdf():
    '''
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    if 'file' not in request.files:
        return redirect('/pdf/view')
    file = request.files['file']
    if file.filename == '':
        return redirect('/pdf/view')
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('./uploads', filename))
        return redirect('/pdf/view')
