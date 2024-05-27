from flask import Flask, request, escape
import re
import requests
from requests.exceptions import Timeout

app = Flask(__name__)

@app.route("/")
def user_page():
    # CWE-79 fix: Use the escape() function to ensure that the user input is securely converted into a string
    user_input = escape(request.args.get("user_input", ""))

    # CWE-918 fix: Validate the URL using regex or similar to ensure it's a site you're OK with before you assemble and make the request
    url = 'https://api.example.com/'
    pattern = re.compile('https://api\\.example\\.com/.+$')

    if not pattern.match(url + user_input):
        return "Sorry, invalid URL!", 400

    try:
        response = requests.get(url + user_input, timeout=5)
    except Timeout as e:
        return 'The request timed out', 408
    return response.text, 200


if __name__ == "__main__":
    # Fix CWE-94 & CWE-215: Set debug=False to avoid exposing the Werkzeug debugger, minimizing arbitrary code execution vulnerability
    app.run(debug=False)