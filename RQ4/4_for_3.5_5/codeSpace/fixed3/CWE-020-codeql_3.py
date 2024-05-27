from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

# Define a list of allowed domains for redirection
allowed_domains = ['example.com', 'trusted-site.org']

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    # Get target URL from the request
    target_url = request.args.get('target')

    if not target_url:
        return "No target URL specified", 400

    # Parse the URL to obtain the domain portion
    domain = urlparse(target_url).hostname

    # Validate that the domain is not None and is in the allowed list
    if domain and domain in allowed_domains:
        return redirect(target_url)
    else:
        return "Redirection to this URL is not allowed", 403

if __name__ == '__main__':
    app.run(debug=False)  # Ensure debug mode is set to False for production