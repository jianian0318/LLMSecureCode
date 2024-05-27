from flask import Flask, request, redirect
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get image file from request and save it to ./pictures folder after encoding
    '''
    file = request.files['file']
    file_data = file.read()
    encoded_data = base64.b64encode(file_data)
    
    with open('./pictures/image.jpg', 'wb') as f:
        f.write(encoded_data)
    
    return redirect('/')