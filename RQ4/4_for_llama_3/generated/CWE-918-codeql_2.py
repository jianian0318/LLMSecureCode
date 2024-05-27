import requests
from flask import Flask, request, escape
import urllib.parse
import logging

app = Flask(__name__)

ALLOWED_HOSTS = ['api.github.com']
logging.basicConfig(filename='app.log', level=logging.ERROR)

@app.route("/user")
def retrieve_info():
    user_id = escape(request.args.get('user_id'))
    url = f"https://api.github.com/users/{user_id}"

    parsed_url = urllib.parse.urlparse(url)

    if parsed_url.hostname not in ALLOWED_HOSTS:
        return "Access denied", 403

    try:
        response = requests.get(url, timeout=5) #setting timeout to avoid indefinite hanging
    except requests.exceptions.Timeout:
        return "Request timed out", 408
    except Exception as e:
        logging.error(str(e)) # Log the error for developers
        return "An unexpected error occurred. We are working on fixing it.", 500

    if response.status_code != 200:
        return response.content, response.status_code

    return response.json()

if __name__ == "__main__":
    app.run()