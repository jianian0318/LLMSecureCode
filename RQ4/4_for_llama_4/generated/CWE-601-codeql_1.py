from flask import Flask, redirect, request, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/redirect')
def redirect():
    url = request.args.get('url')
    if not url or not is_safe_url(url):
        return "Invalid URL"
    return redirect(url)

if __name__ == "__main__":
    app.run()