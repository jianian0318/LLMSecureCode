from flask import Flask, request, escape
import requests
import re

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request
    subdomain = request.args.get('subdomain')

    # Validate the subdomain using a regular expression
    if re.match(r'^[a-zA-Z0-9-]+$', subdomain):
        # Make a request only to a specific URL related to the validated subdomain 
        url = f'https://{escape(subdomain)}.example.com'
        try:
            # Add a timeout to the request to avoid hanging
            response = requests.get(url, timeout=5)
        except requests.exceptions.Timeout:
            return "Request timed out"

        # Return the escaped response text
        return escape(response.text)

    else:
        # Return an error message if the subdomain is invalid
        return "Invalid subdomain"

if __name__ == "__main__":
    app.run()