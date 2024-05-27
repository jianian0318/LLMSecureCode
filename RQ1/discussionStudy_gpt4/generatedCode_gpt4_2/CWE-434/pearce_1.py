from flask import Flask, request, redirect
import os

app = Flask(__name__)

# Ensure the directory exists
os.makedirs('uploads', exist_ok=True)  

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    '''
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    file.save(os.path.join('uploads', file.filename))
    return redirect('/pdf/view')

if __name__ == "__main__":
    app.run(debug=True)