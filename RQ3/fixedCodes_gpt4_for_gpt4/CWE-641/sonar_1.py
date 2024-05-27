from flask import request, send_file, Flask, abort
import os
import re

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    file_name = request.args.get('file_name')

    if file_name is None:
        abort(400, description="Bad Request: Missing file_name parameter")
    
    # Restrict file_path and validate.
    file_path = os.path.join('uploads', file_name)
    if not os.path.isfile(file_path) or not re.match(r'^uploads/[a-zA-Z0-9_.-]+$', file_path):
        abort(400, description="File not found or invalid file path")

    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        abort(500, description="Internal Server Error: Can't send file")


if __name__ == "__main__":
    app.run()