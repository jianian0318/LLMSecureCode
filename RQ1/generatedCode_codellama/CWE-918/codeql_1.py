import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args.get('subdomain')
    url = f"http://{subdomain}.example.com"
    response = requests.get(url)
    return response.content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
