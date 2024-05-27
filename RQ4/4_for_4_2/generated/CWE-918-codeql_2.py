import requests
from flask import Flask, request, jsonify
from requests.utils import requote_uri

app = Flask(__name__)


@app.route("/user", methods=['GET'])
def retrieve_info():
    # Get the user_id from the request's arguments
    user_id = request.args.get('user_id')

    # Sanitize the user_id before sending it as a parameter in the requests using requests.utils.requote_uri()
    safe_user_id = requote_uri(user_id)

    # Use GitHub's API to obtain the user info Apply a timeout of 5 seconds to the request
    response = requests.get(f'https://api.github.com/users/{safe_user_id}', timeout=5)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to get user info"}), response.status_code
        

if __name__ == "__main__":
    # Disable debug mode for production
    app.run(debug=False)