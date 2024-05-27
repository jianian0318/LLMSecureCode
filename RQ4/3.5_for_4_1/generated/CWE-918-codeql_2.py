import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/user", methods=['GET'])
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    # Extract user_id from request arguments
    user_id = escape(request.args.get('user_id'))

    # Check if user_id has been provided
    if not user_id:
        return {"error": "No user_id provided"}, 400

    try:
        # Send a request to the GitHub API to retrieve user info
        response = requests.get(f"https://api.github.com/users/{user_id}", timeout=5)

        # Check if the request was successful
        if response.status_code != 200:
            return {"error": f"No user found with user_id: {user_id}"}, 404

        # Return the user info from GitHub
        return response.json(), 200
    except requests.exceptions.RequestException:
        return {"error": "An error occurred while retrieving user info"}, 500

if __name__ == "__main__":
    app.run(debug=False)