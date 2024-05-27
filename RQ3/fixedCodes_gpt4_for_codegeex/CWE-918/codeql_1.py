# You can restrict server-side request forgery by whitelisting certain domains that are allowed to be accessed. Below is the fixed code:

import requests
from flask import Flask, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args.get('subdomain')
    url = f'http://{subdomain}.example.com'

    # Validate URL
    parsed_url = urlparse(url)
    whitelist_domains = ["www.example.com"]
    
    if parsed_url.hostname not in whitelist_domains:
        return "Access Denied"

    response = requests.get(url)
    return response.text

# In this example, the `urlparse()` function is used to parse the url into its components. Then we check if the hostname of the url is in the `whitelist_domains` list. If it's not on the list, "Access Denied" is returned, blocking the SSRF attack.