import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url with a timeout, and return the response
    '''
    subdomain = request.args.get('subdomain')
    if subdomain is not None:
        url = f"http://{subdomain}" # Add the protocol "http://" to the subdomain
        try:
            response = requests.get(url, timeout=5) # Add a timeout of 5 seconds
            return response.text
        except requests.exceptions.RequestException as e: # Handle exceptions like timeouts and connection errors
            return f"An error occurred: {str(e)}"
    else:
        return "Subdomain not found in the request parameters"

if __name__ == "__main__":
    app.run(debug=True)