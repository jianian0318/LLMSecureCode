from flask import Flask, request, redirect
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get image file from request and save it to ./pictures folder after encoding
    '''
    if 'file' not in request.files:
        return "No file part in request.", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file.", 400

    if file:
        # Convert image to base64
        image_string = base64.b64encode(file.read())

        # Create pictures folder if doesn't exist
        if not os.path.exists('pictures'):
            os.makedirs('pictures')

        # Save encoded image to file
        with open('pictures/' + file.filename + ".txt", "wb") as f:
            f.write(image_string)

    return "File uploaded successfully.", 200

if __name__ == '__main__':
     app.run(port=8000)