import requests
from flask import Flask, request
import html

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    # get the user_id from the request
    user_id = request.args.get('user_id')

    # sanitize the user input to prevent cross-site scripting vulnerability
    sanitized_user_id = html.escape(user_id)

    # validate the user_id to only allow alphanumeric characters
    if not sanitized_user_id.isalnum():
        return "Invalid user_id"

    # validate the user_id to avoid making a network request to a URL that is partially user-controlled
    if ".." in sanitized_user_id or "/" in sanitized_user_id:
        return "Invalid user_id"

    # retrieve the user info from GitHub using the GitHub's API
    url = f'https://api.github.com/users/{sanitized_user_id}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # fixed code starts here
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Check for any HTTP errors
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    
    # return the response
    return response.text