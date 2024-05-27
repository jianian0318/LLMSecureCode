from flask import Flask, request, redirect
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get image file from request and save it to ./pictures folder after encoding
    '''
    
    if 'image' not in request.files:
        return 'No image part', 400

    image = request.files['image']

    #check if the file is one of the allowed type
    if image and allowed_file(image.filename):
        
        # Create the folder if not exist
        if not os.path.exists('./pictures'):
            os.makedirs('./pictures')
        
        image_data = base64.b64encode(image.read())
        image_name = '/pictures/' + image.filename
        
        with open('.'+image_name, 'wb') as image_file:
            image_file.write(image_data)

        return "File saved successfully"

def allowed_file(filename):
    '''Check the extensions of uploaded files'''
    allowed_extensions = set(['png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

if __name__ == "__main__":
    app.run(debug=True)