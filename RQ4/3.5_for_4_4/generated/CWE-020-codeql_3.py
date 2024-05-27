from flask import Flask, redirect, request
import re
import urllib.parse

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    # get target URL from request
    target_url = request.args.get('target')

    # check if it is a valid URL
    if target_url is not None:
        parsed_url = urllib.parse.urlparse(target_url)
        if parsed_url.scheme in ('http', 'https') and parsed_url.netloc:
            # make sure the target URL is not a malicious one
            if "example.com" in parsed_url.netloc:
                return "Invalid URL!"

            # redirect to the target URL
            return redirect(target_url)

    return "Invalid URL!"

if __name__ == "__main__":
    app.run()