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

    user_id = request.args.get('user_id')
    response = requests.get(f'https://api.github.com/users/{user_id}')
    
    return response.json(), response.status_code