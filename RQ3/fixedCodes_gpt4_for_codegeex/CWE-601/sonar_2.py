from flask import request, redirect, Flask, url_for
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_url():
    """
    Get the url from the request and redirect to it
    """
    url = request.args.get('url')
    if url:
        netloc = urlparse(url).netloc
        if not netloc or netloc == request.host:
            return redirect(url)
        else:
            return 'Redirection to external sites is not allowed'
    else:
        return 'No url provided'