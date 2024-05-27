import os
from flask import jsonify, Flask, request

app = Flask(__name__)

SAFE_USER_PATHS = {
    # These are sample usernames and their corresponding safe directory paths
    "alice": "/home/alice",
    "bob": "/home/bob",
    # Add more valid usernames and their home directories
}


@app.route('/reply', methods=['GET'])
def list_files():
    username = request.args.get('username')
    if not username:
        return jsonify({"status": 400, "message": "Username not provided"}), 400

    username = username.strip()
    if username not in SAFE_USER_PATHS:
        return jsonify({"status": 400, "message": "Invalid username provided"}), 400

    home_dir = SAFE_USER_PATHS[username]
    if not os.path.isdir(home_dir):
        return jsonify({"status": 404, "message": f"User's home directory {home_dir} does not exist"}), 404

    if not os.access(home_dir, os.R_OK):
        return jsonify({"status": 403, "message": f"User's home directory {home_dir} is not readable"}), 403

    files = os.listdir(home_dir)
    files = [f for f in files]
    escaped_files = [html.escape(f) for f in files]  # HTML escaping to prevent XSS

    return jsonify({"status": 200, "message": "List of files", "files": escaped_files}), 200


if __name__ == '__main__':
    app.run()