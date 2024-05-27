import requests
from flask import Flask, request, escape
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    user_id = escape(request.args.get('user_id')) # Escaping user input to avoid XSS attack
    url = f"https://api.github.com/users/{user_id}"
    
    parsed_url = urlparse(url) # Parsing the URL to validate/sanitize
    
    if parsed_url.scheme not in ['http', 'https']: # Confirming the URL is http or https
        return 'Invalid Url', 400
    
    try:
        response = requests.get(url, timeout=5) # Added timeout to resolve CWE-400
        return response.json()
    except requests.exceptions.Timeout:
        return 'Request Timed Out', 408

if __name__ == "__main__":
    app.run()