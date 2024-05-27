import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = escape(request.args.get('subdomain'))

    if subdomain and subdomain.isalpha():
        url = f"http://{subdomain}.example.com"  
    else:
        return "Invalid subdomain."

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return "The request timed out. Please try again later."
    except requests.exceptions.TooManyRedirects:
        return "Too many redirects have occurred. Please check your URL."
    except requests.exceptions.RequestException:
        # Use a generic error message to prevent information leakage
        return "An error occurred while processing your request. Please try again later."

    return response.text

if __name__ == "__main__":
    app.run(debug=False)  # Set debug to False in a production environment