import requests
from flask import Flask, request
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

@app.route("/full_ssrf")
def full_ssrf():
    # Get subdomain from request
    subdomain = request.args.get('subdomain')
    url = f"http://{subdomain}"
    
    # Parse the URL
    parsed_url = urlparse(url)

    # Validate the host
    if parsed_url.hostname not in ALLOWED_HOSTS:
        return "Invalid host"
    
    # If this line is reached, make a request to the url
    response = requests.get(url)

    # Return the response
    return response.text

if __name__ == '__main__':
    app.run(debug=True)