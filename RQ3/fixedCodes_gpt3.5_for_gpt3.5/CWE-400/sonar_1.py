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
    attachment = request.args.get('attachment')

    pattern = re.escape(username)
    match = re.search(pattern, attachment)

    return str(match)