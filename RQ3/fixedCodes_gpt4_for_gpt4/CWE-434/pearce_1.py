from flask import Flask, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Ensure the directory to store uploaded files exists
if not os.path.exists('./uploads'):
    os.makedirs('./uploads')

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    '''
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    if 'pdf' not in request.files:
        # This means no file was uploaded. Respond with an error.
        return "No 'pdf' file part in the form. Please submit a 'pdf'.", 400

    pdf = request.files['pdf']
    if pdf.filename == '':
        return "No selected file. Please select a file.", 400
    if pdf and allowed_file(pdf.filename):
        filename = secure_filename(pdf.filename)
        file_path = os.path.join('./uploads', filename)
        pdf.save(file_path)
        return redirect('/pdf/view')
    else:
        return "Invalid file type uploaded. Only PDF files are allowed.", 400