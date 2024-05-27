import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    user_id = request.args.get('user_id')  # get the user_id from the request

    if user_id is not None:
        # Sanitize user_id to prevent any potential security issues
        cleaned_user_id = user_id.strip()

        if cleaned_user_id != "":
            url = "https://api.github.com/users/" + cleaned_user_id  # retrieve user info from GitHub using the API

            try:
                # Set timeout to prevent requests from hanging indefinitely
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    sanitized_data = {
                        "name": data["name"],
                        "email": data.get("email"),
                        "bio": data.get("bio")
                    }
                    return jsonify(sanitized_data)  # return the sanitized user info as JSON
                else:
                    # Return error message and status code from the API response
                    return jsonify({"error": "Request failed.", "status_code": response.status_code}), response.status_code
            except requests.exceptions.RequestException:
                # Handle any request exceptions
                return jsonify({"error": "Request failed.", "status_code": 500}), 500

    return jsonify({"error": "Invalid user_id.", "status_code": 400}), 400