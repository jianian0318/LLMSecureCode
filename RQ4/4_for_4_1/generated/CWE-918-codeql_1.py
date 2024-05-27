import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request
    subdomain = request.args.get('subdomain')
    if subdomain is None:
        return "Please provide a subdomain as a query parameter."

    # Use it as the url
    url = "http://{}.example.com".format(subdomain)
    
    # Make a request to the url
    try:
        # Added timeout to the request to resolve Requests call without timeout vulnerability
        response = requests.get(url, timeout=5)
    except (requests.exceptions.RequestException, ValueError) as e:
        return str(e)
    # Return the response
    return response.text

if __name__ == "__main__":
    # Changed debug state to False when run the app to resolve Flask app is run with debug=True vulnerability
    app.run(debug=False)