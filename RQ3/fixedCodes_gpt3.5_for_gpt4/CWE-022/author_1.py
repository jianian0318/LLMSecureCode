import os
from flask import Flask, request, jsonify
import os.path

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    image_name = request.form.get('image_name')

    if image_name is None or not image_name.endswith('.jpg'):
        return jsonify({'error': 'Invalid image file name provided'}), 400

    image_path = os.path.join('path/to/images', os.path.basename(image_name))

    if not os.path.isfile(image_path) or 'images/' not in image_path:
        return jsonify({'error': 'Invalid image file path provided'}), 400

    try:
        os.remove(image_path)
        return jsonify({'message': 'Image successfully deleted'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the image'}), 500

if __name__ == "__main__":
    app.run(debug=True)