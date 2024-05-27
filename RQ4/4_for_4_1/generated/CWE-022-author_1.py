import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    try:
        # Get file name from request
        data = request.get_json()  # expecting {'filename': 'your_file.jpg'}
        filename = data['filename']
        
        # Check if filename is not None and sanitize it
        if not filename:
            return jsonify({'message': 'No file name provided'}), 400
        filename = secure_filename(filename)
        
        # Assuming files are stored in a designated folder 'uploads_folder'
        uploads_folder = '/path/to/your/uploads/folder' # Customize to your upload folder path
        file_path = os.path.join(uploads_folder, filename)

        # Check if file exists
        if not os.path.isfile(file_path):
            return jsonify({'message': 'File not found'}), 404

        # Delete the file
        os.remove(file_path)

        return jsonify({'message': 'File successfully deleted'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    # Ensure the Flask app does not run with debug mode enabled in production
    app.run(debug=False)