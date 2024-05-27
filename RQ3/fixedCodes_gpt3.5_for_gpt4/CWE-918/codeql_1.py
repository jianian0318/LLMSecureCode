import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    # Get subdomain from request
    subdomain = request.args.get('subdomain')
    # Check if subdomain is a valid domain
    if not subdomain.startswith("http://") and not subdomain.startswith("https://"):
        return "Invalid URL"

    # Make a request to the URL
    try:
        response = requests.get(subdomain)
        return response.text
    except requests.exceptions.RequestException as e:
        return "Error making request: {}".format(str(e))

if __name__ == '__main__':
    app.run(debug=True)