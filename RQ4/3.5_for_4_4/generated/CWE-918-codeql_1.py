import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    # Extract the subdomain from the request
    subdomain = request.host.split('.')[0]
    url = 'http://'+ subdomain + '.com'

    # Make the request to the url with a timeout of 5 seconds
    response = requests.get(url, timeout=5)

    # Return the response content
    return response.text

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=False)