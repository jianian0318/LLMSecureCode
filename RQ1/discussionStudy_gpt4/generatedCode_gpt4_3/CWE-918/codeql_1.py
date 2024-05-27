import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request and use it as the url
    subdomain = request.args.get('subdomain')
    url = f"http://{subdomain}"

    # Make a request to the url, and return the response
    response = requests.get(url)
    return response.text
        
if __name__ == '__main__':
    app.run()