import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request
    subdomain = request.args.get('subdomain')
    url = f"http://{subdomain}"
    
    # Make a request to the url
    response = requests.get(url)
    
    # Return the response
    return response.text

if __name__ == "__main__":
    app.run()