import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    # get image name from post request
    image_name = request.form.get('image_name', None)
    
    # basic request validation
    if image_name is None:
        return jsonify({"error": "Missing image name"}), 400
    
    # specify the path where the image resides (change according to your directory structure)
    image_path = os.path.join("images", image_name)
    
    # delete file if it exists
    if os.path.isfile(image_path):
        os.remove(image_path)
        return jsonify({"success": f"Deleted {image_name} successfully."}), 200
    else:
        return jsonify({"error": f"{image_name} does not exist."}), 404


if __name__ == "__main__":
    app.run(debug=True)