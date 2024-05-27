import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args.get('subdomain')

    if subdomain is None:
        return "Subdomain parameter is missing"

    if not subdomain.isalnum():
        return "Invalid subdomain"

    url = f'https://{subdomain}.example.com'

    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"