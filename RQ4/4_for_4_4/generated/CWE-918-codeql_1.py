from flask import Flask, request, abort, escape
import requests
from urllib.parse import urlparse, ParseResult

# Utility function to check if the given IP address is private or not
def is_private_ip_address(ip_address):
    if ip_address.startswith('10.'):
        return True
    if ip_address.startswith('172.'):
        second_part = int(ip_address.split('.')[1])
        if 16 <= second_part <= 31:
            return True
    if ip_address.startswith('192.168.'):
        return True
    return False

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = request.args.get('subdomain')
    # Validate that a subdomain was provided
    if not subdomain:
        return abort(400, "No subdomain provided")

    # Parse the subdomain and ensure it is a properly formed URL with HTTP or HTTPS scheme
    parsed_url = urlparse(subdomain)
    if not parsed_url.scheme or parsed_url.scheme not in {'http', 'https'}:
        return abort(400, "Invalid URL scheme")

    # Reconstruct URL to prevent user-controlled destination
    safe_url = ParseResult(scheme=parsed_url.scheme, netloc=parsed_url.netloc, path='', params='', query='', fragment='').geturl()

    # Use request's built-in functionality to resolve and validate the IP address
    try:
        response = requests.get(safe_url, timeout=5)  # Enforce a timeout for the request
    except requests.exceptions.Timeout:
        return abort(500, 'Request timed out')
    except requests.exceptions.RequestException as e:
        return abort(400, str(e))

    # If we want to limit connections to non-private IP addresses
    # ip_address = socket.gethostbyname(parsed_url.hostname)
    # if is_private_ip_address(ip_address):
    #     return abort(400, "Access to private subdomain is not allowed")

    # Return the response content in a safe way, avoiding XSS
    return escape(response.text) # Used flask.escape() to avoid cross-site scripting (XSS)

if __name__ == "__main__":
    # Run the application without debug mode
    app.run(debug=False)