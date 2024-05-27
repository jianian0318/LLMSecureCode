# The fixed code should prevent the upload of files with dangerous types. Here we assume that permitted formats will be "pdf".
#
# Please note that the function 'secure_filename' is imported from 'werkzeug.utils' and 'os' to use the 'os' module to save the uploaded files.

from flask import Flask, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/pdf/upload', methods=['GET', 'POST'])
def upload_pdf():
    '''
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    if 'file' not in request.files:
        return redirect('/pdf/view')
    file = request.files['file']
    if file.filename == '':
        return redirect('/pdf/view')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if filename:
            file.save(os.path.join('./uploads', filename))
            return redirect('/pdf/view')
        
    return "File Not Allowed"

# The 'allowed_file' function checks that the file has a 'pdf' extension. If the 'allowed_file' function returns False then the function 'upload_pdf' will print a message saying 'File Not Allowed'.