import os
from flask import Response, request, Flask
import re

app = Flask(__name__)

def is_safe_path(basedir, path, follow_symlinks=True):
    # resolves symbolic links
    if follow_symlinks:
        return os.path.realpath(path).startswith(basedir)
    return os.path.abspath(path).startswith(basedir)

def secure_path(path):
    if path is None or not re.match(r'^[\w-]+$', path):
        return False
    basedir = '/home/'
    full_path = os.path.join(basedir, path)
    return full_path if is_safe_path(basedir, full_path) and os.path.exists(full_path) else False

@app.route('/reply')
def listFiles():
    username = request.args.get('username')
    directory = secure_path(username)
    if directory is False:
        return "Invalid path", 403 # Return 403 Forbidden if the path is not secure
    files = os.listdir(directory)
    return Response(str(files), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)