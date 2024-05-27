import requests
from flask import Flask, request
from jinja2 import escape
import time

app = Flask(__name__)
# Define approved subdomains
approved_subdomains = ['sub1', 'sub2', 'sub3'] 

@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request and use it as the url
    subdomain = escape(request.args.get('subdomain'))

    # If subdomain is None or not in approved list, return a 400 response
    if subdomain is None or subdomain not in approved_subdomains:
        return 'Invalid or no subdomain provided', 400
    
    url = 'http://{}.example.com'.format(subdomain)

    # Make a request to the url with a timeout
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return 'The request timed out', 408

    # Return the response
    return escape(response.text)

if __name__ == "__main__":
    app.run()