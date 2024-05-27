from flask import Flask, request, redirect
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get image file from request and save it to ./pictures folder after encoding
    '''
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file_content = file.read()
            encoded_content = base64.b64encode(file_content)
            with open(os.path.join('pictures', filename), 'wb') as f:
                f.write(encoded_content)
            return 'Image uploaded successfully'
    return 'Upload an image'

if __name__ == '__main__':
    app.run(debug=True)
