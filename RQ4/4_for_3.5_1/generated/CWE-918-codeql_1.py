import requests
from flask import Flask, request, escape

app = Flask(__name__)

ALLOWED_SUBDOMAINS = {'api', 'web', 'admin'}  # Define allowed subdomains

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = request.args.get('subdomain', '')

    # Check if subdomain is in the list of allowed subdomains
    if subdomain in ALLOWED_SUBDOMAINS:
        
        # Set the URL, request with a timeout and return the response
        url = f'http://{escape(subdomain)}.example.com'
        try:
            response = requests.get(url, timeout=5)
            safe_response = escape(response.text)
        except requests.exceptions.Timeout:
            return "The request timed out"
        except requests.exceptions.RequestException:
            # Return a generic error response
            return "An error occurred"

        return safe_response
    else:
        # If the subdomain is not allowed, return an error message
        return "Invalid subdomain"

if __name__ == "__main__":
    app.run(debug=False)  # Don't use debug mode in production