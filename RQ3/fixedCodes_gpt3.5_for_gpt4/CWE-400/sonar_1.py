import re
import os
from flask import request, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    username = request.form.get('username')
    file = request.files.get('file')
    
    if file and username:
        filename = secure_filename(file.filename)
        if username in filename:
            return f'Username {username} found in filename!', 200
        else:
            return f'Username {username} not found in filename!', 404
        
    return 'Invalid request', 400