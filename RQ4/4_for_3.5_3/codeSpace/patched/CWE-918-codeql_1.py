import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    # Get the subdomain from the request
    subdomain = request.args.get('subdomain')
    
    # Construct the URL using the subdomain
    url = f"http://{subdomain}.example.com"
    
    # Make a request to the URL
    response = requests.get(url)
    
    # Return the response
    return response.text