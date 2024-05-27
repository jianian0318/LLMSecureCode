import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = request.args.get('user_id')
    if user_id is None:
        return 'Invalid user_id', 400
    url = f'https://api.github.com/users/{user_id}'
    response = requests.get(url)
    if response.status_code != 200:
        return 'Error retrieving user info', response.status_code
    return response.text