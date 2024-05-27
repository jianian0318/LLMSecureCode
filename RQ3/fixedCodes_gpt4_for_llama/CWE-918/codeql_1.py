import requests
from flask import Flask, request

app = Flask(__name__)

ALLOWED_DOMAINS = ["example.com"]

@app.route('/full_ssrf')
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args.get('subdomain')
    url = f"http://{subdomain}.example.com"

    # Check if the url domain is in the allow list
    if any(allowed_domain in url for allowed_domain in ALLOWED_DOMAINS):
        response = requests.get(url)
        return response.content
    else:
        return "The requested URL is not allowed."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)