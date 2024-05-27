from flask import Flask, redirect, request
import re
import urllib.parse

app = Flask(__name__)

@app.route('/redirect')
def external_url():
    target_url = request.args.get('url', '')

    # Regex to verify the URL format with a stricter pattern that prevents overly permissive ranges
    url_format = re.compile(
        r'https?://'  # http scheme
        r'(?:[a-zA-Z0-9-]+\.?)+'  # domain
        r'(?:\:[0-9]+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # path

    # Match the URL with the full string
    if url_format.fullmatch(target_url):
        # Only allowing redirection to known web pages or domains
        allowed_hosts = ["known_website1.com", "known_website2.com"]
        # Parsing url to get base domain
        parsed_url = urllib.parse.urlparse(target_url)
        if parsed_url.netloc in allowed_hosts:
            return redirect(target_url)
        else:
            return "Redirection to the provided URL not allowed!", 403
    else:
        return "Invalid URL provided!", 400

if __name__ == '__main__':
    app.run(debug=False)