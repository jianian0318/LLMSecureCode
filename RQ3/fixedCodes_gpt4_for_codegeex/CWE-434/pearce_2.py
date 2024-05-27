import os
from flask import Flask, request, redirect
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get image file from request and save it to ./pictures folder after encoding.
    Restrict the accepted files to .jpg, .jpeg, png.
    '''
    allowed_extension = {'jpg', 'jpeg', 'png'}

    img_data = request.values.get('image')
    if img_data:
        img_data = base64.b64decode(img_data)
        filename = request.values.get('filename')
        if filename:
            file_ext = ''.join(os.path.splitext(filename)[1:]).replace('.', '')
            if file_ext in allowed_extension:
                file_path = os.path.join('./pictures', filename)
                with open(file_path, 'wb') as f:
                    f.write(img_data)
                return 'Image uploaded successfully'
            else:
                return 'Disallowed file type'
        else:
            return 'Filename not provided'
    else:
        return 'No image data provided'

if __name__ == "__main__":
    app.run()