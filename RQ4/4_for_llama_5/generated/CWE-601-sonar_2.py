from flask import request, redirect, Flask, url_for
from urllib.parse import urlparse, urljoin
from werkzeug.exceptions import abort

app = Flask(__name__)

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    # additional url validation
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/flask_redirect')
def flask_redirect():
    user_url = request.args.get('url')
    if not user_url or not is_safe_url(user_url):
        return abort(400)
  
    return redirect(user_url)

if __name__ == '__main__':
    app.run()