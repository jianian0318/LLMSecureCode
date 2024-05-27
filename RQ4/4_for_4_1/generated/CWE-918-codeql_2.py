import requests
from flask import Flask, request

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

    # Exception handling if user_id is not provided
    if not user_id:
        return {"message": "Error: user_id not provided."}, 400

    # Accessing GitHub's API to retrieve user info
    try:
        response = requests.get(f'https://api.github.com/users/{user_id}', timeout=5)  # Added a timeout
        return response.json(), 200
    except requests.exceptions.RequestException as e:
        return {"message": f"Error: {e}"}, 500


if __name__ == "__main__":
    app.run()