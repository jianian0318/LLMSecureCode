from flask import Flask, request, escape
import requests
import re

app = Flask(__name__)


@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request
    subdomain = request.args.get('subdomain')

    # Sanitize the subdomain using the escape function to avoid XSS
    sanitized_subdomain = escape(subdomain)

    # Validate the subdomain using a regular expression
    if not re.match(r'^[a-z0-9-]+$', sanitized_subdomain):
        return "Invalid subdomain", 400

    # Make a request to the url and return the response
    url = f"https://{sanitized_subdomain}.example.com"
    return requests.get(url, timeout=5).content  # Request with 5-second timeout


if __name__ == "__main__":
    app.run()