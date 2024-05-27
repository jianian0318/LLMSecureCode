import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    # Get subdomain from request
    subdomain = request.args.get('subdomain')
    # Formulate URL
    url = f"http://{subdomain}"
    # Make a request to the url
    response = requests.get(url)
    # Return the response
    return response.text

if __name__ == '__main__':
    app.run(debug=True)