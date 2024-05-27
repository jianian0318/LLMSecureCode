import requests
from flask import Flask, request, escape

app = Flask(__name__)

# Set a list of allowed subdomains for validation
ALLOWED_SUBDOMAINS = {'api', 'blog', 'www'}
DEFAULT_TIMEOUT = 5  # Timeout in seconds

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request, validate it, make a request to the URL using the valid subdomain,
    and safely return the escaped response to avoid XSS.
    '''
    # Get the subdomain from the request
    subdomain = request.args.get('subdomain')
    
    # Validate subdomain
    if subdomain not in ALLOWED_SUBDOMAINS:
        return "Invalid subdomain", 400
    
    # Construct the URL using the subdomain, preventing SSRF by validating the subdomain
    url = f"http://{subdomain}.example.com"
    
    # Make a request to the URL with a timeout to avoid hanging
    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
    except requests.exceptions.RequestException:
        return "Failed to retrieve data.", 500
    
    # Return the escaped response text to mitigate XSS vulnerabilities
    return escape(response.text)