import requests
from flask import Flask, request, escape

app = Flask(__name__)

# Simple domain whitelist for demonstration purposes
ALLOWED_DOMAINS = {'trustedsub1', 'trustedsub2.example.com'}

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request, validate it against a whitelist,
    construct the URL using a safe scheme, make the request with timeout,
    and return the sanitized response
    '''
    subdomain = request.args.get('subdomain')
    full_domain = f"{subdomain}.example.com"
    if full_domain in ALLOWED_DOMAINS:
        url = f"https://{full_domain}"
        try:
            response = requests.get(url, timeout=5)  # Set timeout to prevent hanging requests
            safe_response = escape(response.text)  # Escape the response to prevent XSS
            return safe_response
        except requests.RequestException as e:
            return f"Failed to retrieve data: {escape(str(e))}", 500
    else:
        return "Subdomain not allowed.", 400

if __name__ == "__main__":
    app.run()