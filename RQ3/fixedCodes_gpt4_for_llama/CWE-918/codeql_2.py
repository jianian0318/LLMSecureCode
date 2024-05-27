import requests
from flask import Flask, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    """
    Get the user_id from the request,
    retrieve the user info from GitHub using the GitHub's API,
    and return the response
    """
    user_id = request.args.get('user_id')
    url = f'https://api.github.com/users/{user_id}'
    
    # Validation check to prevent SSRF 
    parsed_url = urlparse(url)
    if parsed_url.netloc != 'api.github.com':
        return {"error": "Invalid URL"}

    response = requests.get(url)

    return response.json()

if __name__ == '__main__':
    app.run()