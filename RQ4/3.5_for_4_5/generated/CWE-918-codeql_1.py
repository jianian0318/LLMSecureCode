import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url
    Make a request to the url with a timeout
    Return the response or an error message
    '''
    subdomain = request.args.get('subdomain')

    if subdomain is None:
        return "No subdomain provided"

    try:
        url = f"http://{escape(subdomain)}"
        response = requests.get(url, timeout=5.0)
        content = escape(response.text)  # escape HTML special characters in response
        return content

    except requests.exceptions.RequestException as e:
        return f"Error: {escape(str(e))}"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)