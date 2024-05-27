import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    then retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = request.args.get('user_id')  # Get the user_id from the request
    url = f"https://api.github.com/users/{user_id}"  # Construct the GitHub API URL
    response = requests.get(url)  # Send a GET request to the GitHub API
    return response.json()  # Return the response as JSON