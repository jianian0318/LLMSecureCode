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
        return "Please provide a valid user_id.", 400
    
    if not isinstance(user_id, str):
        return "Invalid user_id type.", 400
    
    try:
        response = requests.get(f'https://api.github.com/users/{user_id}')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return str(e), 500

    return response.json(), response.status_code