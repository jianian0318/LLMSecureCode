from flask import Flask, request, redirect
import os

app = Flask(__name__)

# Ensure the directory to store uploaded files exists
if not os.path.exists('./uploads'):
    os.makedirs('./uploads')

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

    file_path = os.path.join('./uploads', pdf.filename)
    pdf.save(file_path)

    return redirect('/pdf/view')