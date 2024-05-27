from flask import Flask, request, redirect
import base64
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './pictures'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/img/upload', methods=['POST'])
def upload_img():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as f:
            f.write(encoded_string)
        return redirect(request.url)
    return "Failed to upload image"

if __name__ == "__main__":
    app.run()