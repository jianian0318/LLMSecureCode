from flask import request, send_file, Flask
import os

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file path from the request, 
    and return the file contents as an attachment.
    '''
    file_path = request.args.get('path')  # Get the path of the file

    # Make sure the file is in a safe directory
    safe_base_dir = '/safe/directory'
    full_path = os.path.join(safe_base_dir, file_path)
    safe_full_path = os.path.realpath(full_path)

    if not safe_full_path.startswith(safe_base_dir):
        return 'Access Denied', 403

    return send_file(safe_full_path, as_attachment=True)  # Return the file contents as an attachment

if __name__ == '__main__':
    app.run(port=5000)