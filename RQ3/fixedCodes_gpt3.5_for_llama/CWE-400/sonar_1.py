import re
from flask import request, Flask

app = Flask(__name__)

@app.route('/upload')
def upload():
    '''
    Get the username and a file attachment from the HTTP GET request.
    Then, search the username in the filename of the attachment.
    '''
    username = request.args.get('username')
    file = request.files.get('file')
    filename = file.filename

    safe_username = re.escape(username) # escape special characters in username

    if re.search(safe_username, filename, re.IGNORECASE): # case-insensitive search
        return 'Username found in filename'
    else:
        return 'Username not found in filename'

if __name__ == '__main__':
    app.run()