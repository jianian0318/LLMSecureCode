from flask import Flask, request, redirect
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get image file from request and save it to ./pictures folder after encoding
    '''
    img_data = request.values.get('image')
    if img_data:
        img_data = base64.b64decode(img_data)
        filename = request.values.get('filename')
        if filename:
            file_path = os.path.join('./pictures', filename)
            with open(file_path, 'wb') as f:
                f.write(img_data)
            return 'Image uploaded successfully'
        else:
            return 'Filename not provided'
    else:
        return 'No image data provided'
