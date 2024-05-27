import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request
    subdomain = request.args.get('subdomain')

    if subdomain:
        # Validating the subdomain to prevent SSRF attacks
        if not isValidSubdomain(subdomain):
            return "Invalid subdomain"

        # Whitelist allowed host names or IP addresses
        allowed_hosts = ['example.com']

        # Check if the subdomain is in the allowed hosts
        if not isAllowedHost(subdomain, allowed_hosts):
            return "Invalid host"

        # use it as the url
        url = f'http://{subdomain}.example.com'

        try:
            # Allow only HTTP and HTTPS requests
            if not url.startswith(("http://", "https://")):
                return "Invalid protocol"

            # Make a request to the url with a timeout of 5 seconds
            response = requests.get(url, timeout=5)

            # Escape HTML characters to prevent XSS attacks
            escaped_response = escape(response.text)

            # Return the escaped response
            return escaped_response

        except requests.exceptions.RequestException as e:
            # Return a generic error message instead of exposing implementation details
            return "An error occurred while making the request"

    else:
        return "No subdomain provided"


# Function to validate the subdomain
def isValidSubdomain(subdomain):
    return all(c.isalnum() or c == '-' for c in subdomain)


# Function to check if the subdomain is in the allowed hosts
def isAllowedHost(subdomain, allowed_hosts):
    for host in allowed_hosts:
        if subdomain.endswith(host):
            return True
    return False

if __name__ == "__main__":
    app.run(debug=False)