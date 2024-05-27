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
    user_id = request.args.get('user_id')
    if user_id is not None:
        response = requests.get(f'https://api.github.com/users/{user_id}')
        return response.json()
    else:
        return {"error": "No user_id provided"}, 400


if __name__ == "__main__":
    app.run(debug=True)


# In this code, we're adding methods=['GET'] to the route decorator to explicitly allow GET requests. We're also using `request.args.get('user_id')` to get the user_id value from the request query parameters. Then, if a user_id is provided, we're using the requests library to send a GET request to the GitHub API, passing along the user_id in the URL. If the user_id is not provided, the application returns an error code 400 and a JSON message indicating the "No user_id provided" error. Finally, we check if the main module is the one being run by Python and, if so, start the Flask application.