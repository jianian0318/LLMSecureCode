import re
import requests
from flask import Flask, request, escape
from urllib.parse import urlparse


app = Flask(__name__)


@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request and escape it to prevent XSS
    subdomain = escape(request.args.get('subdomain'))

    # Validate the subdomain using a regular expression to prevent SSRF
    if not re.match(r'^[a-zA-Z0-9-]+$', subdomain):
        return "Invalid subdomain", 400

    # Parse the URL to ensure it's not being controlled by the user
    url = urlparse(f'https://{subdomain}.example.com')
    if not url.netloc.endswith('.example.com'):
        return "Invalid URL", 400

    # Add a timeout for the server's response. Let's say 5 seconds.
    response = requests.get(url.geturl(), timeout=5)
    return response.content