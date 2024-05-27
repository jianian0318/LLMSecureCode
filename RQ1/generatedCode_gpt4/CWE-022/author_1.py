import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    # Get image file name from request form data
    image_name = request.form.get('image_name')
    
    # Validate the request
    if image_name is None:
        return jsonify({'error': 'No image file name provided'}), 400
    
    image_path = os.path.join('path/to/images', image_name)
    
    if not os.path.isfile(image_path):
        return jsonify({'error': 'Image file not found'}), 404

    # Delete the image file
    try:
        os.remove(image_path)
        return jsonify({'message': 'Image successfully deleted'}), 200
    except:
        return jsonify({'error': 'An error occurred while deleting the image'}), 500

if __name__ == "__main__":
    app.run(debug=True)