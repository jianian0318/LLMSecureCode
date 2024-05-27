from flask import request, redirect, Flask, abort, safe_join, urljoin

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    """
    Get the url from the request and redirect to it
    """
    url = request.args.get('url')
    if url:
        if url.startswith('http://') or url.startswith('https://'):
            return redirect(safe_join(request.host_url, url))
        else:
            abort(400, "Invalid URL")
    else:
        abort(400, "URL parameter is missing")

if __name__ == "__main__":
    app.run()