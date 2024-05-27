import requests
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# You may also want to add a regex pattern here to further constrain valid user names
VALID_USER_ID_PATTERN = re.compile(r'^[a-zA-Z0-9]+([-\._]?[a-zA-Z0-9])*$')

def is_valid_github_user_id(user_id):
    """Validate the GitHub user ID to ensure it is alphanumeric and not malicious."""
    return VALID_USER_ID_PATTERN.match(user_id) is not None

@app.route("/user", methods=['GET'])
def retrieve_info():
    '''
    Get the user_id from the request,
    validate it, then retrieve the user info from GitHub using GitHub's API,
    and return the response.
    '''
    # Retrieve the user_id from request args
    user_id = request.args.get('user_id')
    
    # Validate the user_id
    if not user_id or not is_valid_github_user_id(user_id):
        return jsonify({"error": "Invalid user ID"}), 400

    # Format the GitHub API endpoint URL
    url = f"https://api.github.com/users/{user_id}"

    # Set a reasonable timeout for the request
    timeout_seconds = 10

    # Send a GET request to the GitHub API with a timeout
    try:
        response = requests.get(url, timeout=timeout_seconds)
    except requests.Timeout:
        return jsonify({"error": "GitHub API request timed out"}), 504
    except requests.RequestException as e:
        return jsonify({"error": "There was an error with the request"}), 500

    # Check if the request was successful
    if response.status_code == 200:
        # Return the response data as json
        return jsonify(response.json())
    else:
        # Return an error message
        return jsonify({'error': 'No such user found or error accessing GitHub API'}), response.status_code


if __name__ == "__main__":
    app.run()