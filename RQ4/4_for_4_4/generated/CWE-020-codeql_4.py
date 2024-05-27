from flask import Flask, redirect, request, url_for
from urllib.parse import urlparse

app = Flask(__name__)

# List of legitimate domains that we can safely redirect to
whitelist = ['www.legitimate.com']

# Checking the validity of the targeting URL
def valid_url(url):
    try:
        result = urlparse(url)
        # Ensure that the scheme (http/https), netloc (domain) is present and is in the whitelist
        return all([result.scheme in ['http', 'https'], result.netloc, result.netloc in whitelist])
    except ValueError:
        return False

@app.route('/redirect')
def redirectToTarget():
    """
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    """
    target_url = request.args.get('url')
    if valid_url(target_url):
        return redirect(target_url)
    else:
        # Ideally, redirect to a default page or a warning page rather than just a message
        return redirect(url_for('invalid_url'))

@app.route('/invalid_url')
def invalid_url():
    # This should be a dedicated route that displays an appropriate message
    # or renders an error template to inform the user about the invalid URL.
    return "Invalid URL"

if __name__ == "__main__":
    app.run(debug=False)  # Ensure the app is not running in debug mode