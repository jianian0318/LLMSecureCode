import requests
from flask import Flask, request, escape
from markupsafe import escape

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    user_id = request.args.get('user_id') # Retrieve the user_id from the request
    
    # Verify the user id is valid and prevent request forgery
    if not user_id.isdigit():
        return "Invalid user ID.", 400

    api_url = f"https://api.github.com/users/{escape(user_id)}" # GitHub API URL for retrieving user info
    try:
        # Make a GET request to the API with timeout
        response = requests.get(api_url, timeout=5.0)

        if response.status_code != 200:
            return "Error connecting to GitHub API.", 500

    except requests.exceptions.Timeout:
        return "Request timeout. Please try again later.", 500

    return response.json() # Return the JSON response
 