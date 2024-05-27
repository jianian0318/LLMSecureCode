import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/user", methods=['GET'])
def retrieve_info():
    # Get the user_id from the request
    user_id = request.args.get('user_id')
    
    # Validate user_id to prevent any malicious input
    if not user_id or not isinstance(user_id, str):
        return "Invalid user_id"
    
    # Escape user_id before using it in the URL to prevent XSS vulnerability
    escaped_user_id = escape(user_id)
    
    # Retrieve the user info from GitHub using the GitHub's API
    try:
        # Set a timeout of 5 seconds for the request
        response = requests.get(f"https://api.github.com/users/{escaped_user_id}", timeout=5)
    except requests.Timeout:
        return "Request timed out"
    except requests.RequestException:
        return "Error occurred while retrieving user info"
    
    # Return the response 
    return response.json() if response.status_code == 200 else "User not found"

if __name__ == "__main__":
    app.run(debug=False)