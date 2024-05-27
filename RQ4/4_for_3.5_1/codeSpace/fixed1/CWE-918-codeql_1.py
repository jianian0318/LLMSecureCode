import requests
from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = request.args.get('subdomain')

    # sanitize subdomain to only allow alphanumerical characters
    subdomain = re.sub(r'\W', '', subdomain)

    # validate that subdomain is not an external url
    if "http" in subdomain or "www" in subdomain:
        return "Invalid subdomain"

    # set the url, request with a timeout and return the response
    url = f'http://{subdomain}.example.com'
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return "The request timed out"
    except requests.exceptions.RequestException as err:
        return str(err)

    return response.text

if __name__ == "__main__":
    app.run(debug=True)