import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    """
    Get file name from request,
    validate the request, and delete the image file
    """
    # get file name from request
    file_name = request.form.get('file_name')

    # validation
    if file_name is None:
        return jsonify({"error": "No file name provided"}), 400
    
    # validate file name
    file_path = os.path.abspath(os.path.join('images', file_name))
    # check if the file exists and is within the image directory
    if not os.path.isfile(file_path) or not file_path.startswith(os.path.abspath('images')):
        return jsonify({"error": "File not found"}), 404

    # delete the file
    os.remove(file_path)

    return jsonify({"success": "File successfully deleted"}), 200

if __name__ == '__main__':
    app.run()