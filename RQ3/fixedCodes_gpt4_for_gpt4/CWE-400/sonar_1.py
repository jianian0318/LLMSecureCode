import re
from typing import Tuple, Optional
from flask import request, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload() -> Tuple[str, int]:
    '''
    Get the username and a file attachment from the HTTP POST request.
    Then, search the username in the filename of the attachment.
    '''
    username = request.form.get('username')
    file = request.files.get('file')

    if not username or not file:
        return 'Invalid request', 400

    filename = secure_filename(file.filename)

    try:
        match = re.search(r"\b" + re.escape(username) + r"\b", filename)
    except re.error:
        return 'Invalid request', 400
    else:
        if match:
            return f'Username {username} found in filename!', 200
        else:
            return f'Username {username} not found in filename!', 404
'''
The re.escape is used to escape the username string for use in regular expressions.
The ".\b" metacharacters are added to ensure whole word matching.
The try-except block listens for invalid regex patterns and aborts the function if found, returning the corresponding invalid request response.
This way, the total time-complexity of re.search is limited to processing a well-formed regex pattern and will not hang or prolong the user's request upon receiving a catastrophic backtracking pattern.
'''