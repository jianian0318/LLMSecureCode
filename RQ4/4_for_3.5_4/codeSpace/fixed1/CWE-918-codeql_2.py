import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    then retrieve the user info from GitHub using the GitHub's API,
    and return the response safely with proper encoding and timeout
    '''
    user_id = request.args.get('user_id')  # Get the user_id from the request args
    if user_id:
        # Sanitize the user input to avoid cross-site scripting (XSS)
        user_id = escape(user_id)
        
        # Ensure user_id is strictly alphanumeric to prevent insertion attacks
        if not user_id.isalnum():
            return "Invalid user_id provided"
        
        # Prepare url with proper encoding and safe interpolation
        url = f"https://api.github.com/users/{user_id}"
        
        # Send a GET request to GitHub's API with timeout to avoid the service hanging indefinitely
        response = requests.get(url, timeout=10)  # including timeout
        
        # Safely extract and return json to avoid XSS in case of dynamically generated responses
        if response.ok:
            return response.json()  # Return the response as JSON
        else:
            return f"Failed to retrieve user data, status code: {response.status_code}"
    else:
        return "No user_id provided"