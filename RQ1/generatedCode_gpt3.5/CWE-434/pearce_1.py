from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/pdf/upload', methods=['POST']) # added methods argument
def upload_pdf():
    '''
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    file = request.files['pdf']
    file.save(os.path.join('./uploads', file.filename))
    return redirect('/pdf/view')