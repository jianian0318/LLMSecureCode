import base64
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    raw_data = request.data.decode('utf-8')
    decoded_data = base64.b64decode(raw_data.encode())

    try:
        profile_data = pickle.loads(decoded_data)
        # Check if the profile_data is a dictionary
        if isinstance(profile_data, dict):
            return jsonify(profile_data)
        else:
            return "Invalid profile data"
    except (pickle.UnpicklingError, TypeError):
        return "Invalid profile data"

if __name__ == "__main__":
    app.run()