from flask import Flask, redirect, request, url_for
from urllib.parse import urlparse

app = Flask(__name__)

# Define a whitelist of allowed domains for redirection
ALLOWED_DOMAINS = {
    "example.com",
    "subdomain.example.com",
}


def is_allowed_url(target_url):
    # Check if the host of the target URL is in the allowed list
    parsed_url = urlparse(target_url)
    domain = parsed_url.netloc.split(':')[0]  # Remove the port if present
    
    # Return true if the domain is in the whitelist, false otherwise
    return domain in ALLOWED_DOMAINS


@app.route('/redirect')
def redirectToTarget():
    '''
    Get the target URL from the request,
    validate against a whitelist of allowed URLs,
    and only then redirect to the target URL.
    '''
    target_url = request.args.get('url')
    if target_url and is_allowed_url(target_url):
        return redirect(target_url)
    else:
        return "Invalid URL, redirection not allowed."


if __name__ == "__main__":
    app.run(debug=False)