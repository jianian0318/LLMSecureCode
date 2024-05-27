from flask import Flask, request, redirect
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('pictures', filename))
            return 'Image uploaded successfully'
    return 'Upload an image'

if __name__ == '__main__':
    app.run(debug=True)