import requests
from flask import Flask, request
import urllib.parse

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = str(request.args.get('subdomain', ''))  # Get the subdomain from the request query parameter
    url = f"http://{subdomain}.example.com"  # Construct the URL with the subdomain

    if not subdomain:
        return "Subdomain parameter is missing.", 400

    # Validate subdomain to prevent SSRF attacks
    if not subdomain.isalnum():
        return "Invalid subdomain.", 400

    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.hostname != "example.com":
        return "Invalid domain in URL.", 400

    try:
        response = requests.get(parsed_url.geturl(), timeout=5)  # Make a GET request to the URL with a timeout of 5 seconds
        return response.text  # Return the response body
    except requests.exceptions.RequestException:
        return "Error making request.", 500