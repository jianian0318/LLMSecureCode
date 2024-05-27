import os
import requests
import flask

app = flask.Flask(__name__)

@app.route("/user", methods=['GET'])
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    try:
        # Get user_id from the request and escape any special characters
        user_id = flask.escape(request.get_json()['user_id'])
    except KeyError:
        return 'User ID not provided', 400

    # Check if user_id is in allowed_users list, to prevent CWE-918
    allowed_users = ["user1", "user2", "user3"]
    if user_id not in allowed_users:
        return 'Invalid User ID', 400

    # Retrieve user info from GitHub
    url = f"https://api.github.com/users/{user_id}"
    try:
        response = requests.get(url, timeout=10.0)
    except requests.exceptions.Timeout:
        return 'Request Timeout', 408

    if response.status_code != 200:
        return f"GitHub API request failed with status code: {response.status_code}", 500
    
    # Return the response
    return response.json()

if __name__ == "__main__":
    # Set flask environment to production
    os.environ["FLASK_ENV"] = "production"

    # Start flask app
    app.run(debug=False)