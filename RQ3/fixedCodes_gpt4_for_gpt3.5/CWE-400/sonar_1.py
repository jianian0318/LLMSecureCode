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

    if len(username) > 1000 or len(attachment) > 1000:
        return 'Invalid request. The username or attachment string is too long.', 400

    pattern = fr'{username}'
    try:
        match = re.search(pattern, attachment)
        return str(match)
    except re.error:
        return 'Invalid request. The regex pattern caused an issue.', 400

if __name__ == "__main__":
    app.run()