import requests
from flask import Flask, request, escape
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = request.args.get('subdomain')
    
    # Parse the URL to extract only the netloc part
    parsed_url = urlparse(f"http://{subdomain}")
    allowed_domains = ["example.com"]  # List of domains you trust for network requests
    if not parsed_url.netloc.endswith(tuple(allowed_domains)):
        return "Error: Invalid subdomain supplied"

    safe_url = f"http://{escaped_subdomain}.example.com"

    try:
        # CWE-400 fix - Add timeout to requests call
        response = requests.get(safe_url, timeout=5)

        # CWE-79 fix - escape the response to prevent potential XSS attacks
        safe_response = escape(response)

        return safe_response
    except requests.exceptions.Timeout:
        return "Error: Request timed out"

if __name__ == "__main__":
    app.run()