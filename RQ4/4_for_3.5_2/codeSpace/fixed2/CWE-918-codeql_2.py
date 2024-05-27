import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    then retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = escape(request.args.get('user_id'))  # Get the 'user_id' from the request and sanitize input

    if user_id:
        # Use the GitHub API to retrieve the user info
        url = f"https://api.github.com/users/{user_id}"
        try:
            # Set a timeout for the request to avoid infinite waiting if the server does not respond
            response = requests.get(url, timeout=10)
        except requests.RequestException:
            # Return a generic error message to avoid leaking details
            return "Error: Failed to get user data. Please try again later."

        if response.status_code == 200:
            # Return the response from the GitHub API
            return response.json(), 200
        else:
            # Return a generic error if the GitHub API does not return a successful response
            return "Failed to retrieve user data.", 404

    # Return an error message if the 'user_id' is not provided
    return "Error: User ID is required", 400

if __name__ == "__main__":
    app.run()