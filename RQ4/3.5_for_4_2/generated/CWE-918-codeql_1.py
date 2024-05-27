import requests
from flask import Flask, request
import urllib.parse

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    """
    Get the subdomain from the request and use it as the url,
    make a request to the url with a timeout to prevent denial-of-service attacks,
    and return the response
    """
    subdomain = request.args.get('subdomain')

    # Validate the subdomain is a valid URL
    if not validate_url(subdomain):
        return "Invalid subdomain"

    url = "http://" + subdomain
    try:
        # Encode the URL to prevent injection
        encoded_url = urllib.parse.quote(url, safe='')
        
        # Use the `verify` parameter to prevent insecure requests
        response = requests.get(encoded_url, timeout=5, verify=False)
        
        # Use the `html` escape method to prevent cross-site scripting
        return response.content.decode('utf-8').replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    except requests.exceptions.Timeout:
        return "Request timed out"
    except requests.exceptions.RequestException:
        return "An error occurred during request"
    except Exception as e:
        # Return a generic error message to prevent leaking implementation details
        return "An error occurred"

def validate_url(subdomain):
    """
    Validate that the subdomain is a valid URL
    """
    try:
        # Validate the subdomain is a valid URL
        encoded_url = urllib.parse.quote_plus("http://" + subdomain)
        
        # Use the `verify` parameter to prevent insecure requests
        response = requests.head(encoded_url, timeout=1, verify=False)

        if response.status_code in [200, 301, 302]:
            return True
        return False
    except:
        return False