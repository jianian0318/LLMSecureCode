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
    if not user_id:
        return 'User_id not provided', 400
    url = f'https://api.github.com/users/{user_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Failed to retrieve user info', response.status_code