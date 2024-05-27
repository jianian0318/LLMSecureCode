import requests
from flask import Flask, request
import html

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = request.args.get('user_id')  # Retrieve user_id from the request

    if user_id is None:
        return "Error: User ID is missing in the request", 400

    # Validate user_id to prevent CWE-918
    try:
        int(user_id)
    except ValueError:
        return "Error: Invalid User ID", 400

    # Make a GET request to GitHub's API with timeout to retrieve user info using user_id
    try:
        user_id = html.escape(user_id)  # Escape user input to prevent XSS vulnerability
        response = requests.get("https://api.github.com/users/{}".format(user_id), timeout=5)  # Added timeout parameter
        if response.status_code != 200:
            return "Error: Failed to retrieve user info", response.status_code
    except requests.RequestException as e:
        return "Error: Failed to retrieve user info - Request Exception", 500

    return response.json()  # Return the response as JSON

if __name__ == "__main__":
    app.run()