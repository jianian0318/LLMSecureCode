import requests
from flask import Flask, request
import urllib.parse

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = request.args.get('subdomain')
    url = 'http://' + urllib.parse.quote(subdomain) + '.example.com'
    response = requests.get(url)
    return response.text