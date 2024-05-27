import requests
from flask import Flask, request, escape
from urllib.parse import urlparse

app = Flask(__name__)

# a list of allowed domains
allowed_domains = ['subdomain1.example.com', 'subdomain2.example.com']

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = escape(request.args.get('subdomain'))
    # Make sure the subdomain is in our list of allowed domains
    if f'{subdomain}.example.com' not in allowed_domains:
        return 'Invalid URL'
    else:
        url = f"http://{subdomain}.example.com"
        parsed_url = urlparse(url)
        # Check the parsed URL to make sure it is legitimate
        if parsed_url.scheme not in ["http", "https"]:
            return 'Invalid URL'
        else:
            # Limit the request to a specific timeout
            response = requests.get(url, timeout=5)
            # Escape the text returned by the request to make sure it's safe
            return escape(response.text)

if __name__ == "__main__":
    # Only allow connections from localhost
    app.run(host='127.0.0.1', port=8080)