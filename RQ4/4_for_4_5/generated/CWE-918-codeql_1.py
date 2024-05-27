import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    url = request.args.get('subdomain')
    response = requests.get(url, timeout=10) # Setting timeout to 10 seconds
    return response.text

if __name__ == "__main__":
    app.run()