import requests
from flask import Flask, request
import html

app = Flask(__name__)

@app.route("/user", methods=['GET'])
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    # Get the user_id from the request
    user_id = request.args.get('user_id')

    # Validate the user_id to prevent request forgery attacks
    if user_id is None or not user_id.isalnum():
        return 'Invalid user_id', 400

    # The GitHub's API URL for user
    url = f"https://api.github.com/users/{user_id}"

    # Validate the URL to prevent CWE-918 vulnerability
    if not url.startswith("https://api.github.com/users/"):
        return 'Invalid URL', 400

    # Retrieve the user info from GitHub using the GitHub's API with a timeout
    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException:
        return 'Failed to retrieve user info', 500

    # Check if the response is successful
    if response.status_code != 200:
        return 'Failed to retrieve user info', 500

    # Encode the user info response to prevent cross-site scripting vulnerabilities
    encoded_response = html.escape(response.text)

    # Return the response
    return encoded_response