import requests
from flask import Flask, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request, and validate if the user id is not structured like a URL,
    then retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = request.args.get('user_id')
    # validate input
    if not validate_user_id(user_id):
        return 'Invalid user id!', 400
    response = requests.get(f'https://api.github.com/users/{user_id}')
    return response.json(), response.status_code

def validate_user_id(user_id):
    '''
    Function to validate user_id. 
    Checks whether it is structured like a URL.
    '''
    try:
        result = urlparse(user_id)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False