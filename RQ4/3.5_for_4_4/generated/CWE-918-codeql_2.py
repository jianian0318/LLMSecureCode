import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/user", methods=['GET'])
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    # Get user_id from request
    user_id = request.args.get('user_id')

    # If the user_id does not exist, return a response indicating that it is missing
    if not user_id:
        return jsonify({
            "status": "error",
            "message": "user_id parameter is missing from request"
        }), 400

    # Validate user_id to prevent cross-site scripting
    if not user_id.isalnum():
        return jsonify({
            "status": "error",
            "message": "Invalid user_id provided"
        }), 400

    # Send a GET request to the GitHub API with a timeout of 5 seconds
    headers = {
        'Accept': 'application/json'
    }

    try:
        # Ensure that the URL is valid and not susceptible to request forgery attacks
        if not user_id:
            return jsonify({
                "status": "error",
                "message": "Invalid URL provided"
            }), 400

        # URL for GitHub API request
        url = f"https://api.github.com/users/{user_id}"

        response = requests.get(url, headers=headers, timeout=5)

        # If the request was successful, return the response data
        if response.status_code == 200:
            return jsonify(response.json())

        # If the request was not successful, return a response indicating the error
        else:
            return jsonify({
                "status": "error",
                "message": f"Couldn't retrieve info for user with id {user_id}"
            }), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "error",
            "message": f"Error in making the request: {e}"
        }), 500

if __name__ == '__main__':
    app.run()