import requests
from flask import Flask, request, escape

app = Flask(__name__)

# Define a set of safe, expected subdomains (should ideally be a restricted, predefined set)
ALLOWED_SUBDOMAINS = {'trustedsub1', 'trustedsub2'}
DOMAIN = "example.com"

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request, validate it against a whitelist,
    construct the URL using a safe scheme, make the request with a timeout,
    and return the sanitized response.
    '''
    subdomain = request.args.get('subdomain')
    safe_subdomain = escape(subdomain)
    
    # Check if the subdomain is in the list of allowed subdomains
    if safe_subdomain in ALLOWED_SUBDOMAINS:
        # Safely construct the full URL
        full_url = f"https://{safe_subdomain}.{DOMAIN}"
        try:
            # Make the HTTP GET request
            response = requests.get(full_url, timeout=5)  # Set timeout to prevent hanging requests
            # Escape the response content to prevent XSS
            safe_response = escape(response.text)
            return safe_response
        except requests.RequestException as e:
            # Handle errors safely
            return f"Failed to retrieve data: {escape(str(e))}", 500
    else:
        # Reject requests with subdomains not in the allowed list
        return "Subdomain not allowed.", 400

if __name__ == "__main__":
    app.run()