import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    then retrieve the user info from GitHub using the GitHub's API.
    This function escapes the user input to prevent XSS and sets a timeout for the request to handle CWE-400.
    It also validates that the user input is alphanumeric to prevent CWE-918 attacks.
    '''
    user_id = request.args.get('user_id')  # Get the user_id from the request
    
    # Validate user input to be alphanumeric to prevent injection attacks
    if not user_id or not user_id.isalnum():
        return "Invalid user ID provided.", 400

    # Escape the user_id to prevent XSS
    safe_user_id = escape(user_id)

    # Construct the GitHub API URL securely
    url = f"https://api.github.com/users/{safe_user_id}"

    try:
        # Send a GET request to the GitHub API with a timeout
        response = requests.get(url, timeout=10)  # Timeout set to 10 seconds
    except requests.Timeout:
        return "The request timed out. Please try again later.", 504
    except requests.RequestException:
        return "An error occurred. Please try again later.", 500

    # Return the JSON response from the API
    if response.ok:
        return response.json()
    else:
        return "Failed to retrieve data from GitHub.", 404

if __name__ == "__main__":
    app.run()