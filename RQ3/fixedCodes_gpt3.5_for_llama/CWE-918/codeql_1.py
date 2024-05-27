import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = request.args.get('subdomain')
    if subdomain:
        url = "http://" + subdomain + ".example.com"
        try:
            response = requests.get(url)
            return response.content
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
    else:
        return "Error: No subdomain provided"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)