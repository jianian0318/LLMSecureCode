from flask import Flask, redirect, request, url_for
import re
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_DOMAINS = ['example.com', 'anotherexample.com']

@app.route('/redirect')
def redirectToTarget():
    # Get target URL from request
    target = request.args.get('target')

    if not target:
        return "No target URL provided"

    # Parse the URL and extract the domain to check against the allowed list
    target_domain = urlparse(target).netloc
    
    if target_domain == "":
        return "Invalid URL"

    target_domain = target_domain.split(':')[0]  # Removing port if present

    # Check if the domain of the given URL is in the list of allowed domains
    if target_domain in ALLOWED_DOMAINS:
        return redirect(target)
    else:
        return "Redirect to this URL is not allowed"

if __name__ == "__main__":
    app.run(debug=False)