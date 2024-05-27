import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    user_id = request.args.get('user_id') # Retrieve the user_id from the request
    api_url = f"https://api.github.com/users/{user_id}" # GitHub API URL for retrieving user info
    response = requests.get(api_url) # Make a GET request to the API

    return response.json() # Return the JSON response