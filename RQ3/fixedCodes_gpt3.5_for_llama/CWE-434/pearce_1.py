from flask import Flask, request, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return redirect('/pdf/view')
    file = request.files['file']
    if file.filename == '':
        return redirect('/pdf/view')
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('./uploads', filename))
        return redirect('/pdf/view')

if __name__ == '__main__':
    app.run()