from flask import Flask, request, redirect, send_from_directory
import os
import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return "No 'pdf' file part in the form. Please submit a 'pdf'.", 400

    pdf = request.files['pdf']
    if pdf.filename == '' or not allowed_file(pdf.filename):
        return "Invalid or No selected file. Please select a PDF file.", 400

    pdf.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename.secure_filename(pdf.filename)))

    return redirect('/pdf/view')

@app.route('/pdf/view/<filename>')
def view_pdf(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()