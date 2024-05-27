import os
from flask import Response, request, Flask, jsonify

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    # Fixed path, thus users can't change the directory path anymore
    directory = f'/home/username/'

    # List all the files and then return the list as a response.
    try:
        file_list = os.listdir(directory)
    except FileNotFoundError:
        return jsonify({"error": f"Directory '{directory}' not found."}), 404

    return jsonify({"files": file_list})

if __name__ == "__main__":
    # Do not run the app in debug mode
    app.run(debug=False)