import re
from flask import request, redirect, Flask, url_for

app = Flask(__name__)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')

    # check if the given url is a relative url, so we can safely redirect to it
    if re.match(r'^/[^/]', url):
        return redirect(url)
    else:
        try:
            host = urlparse(url).hostname
        except Exception:
            return redirect(url_for('error_redirect'))

        # check if the host is in the ALLOWED_HOSTS and redirect
        if host in ALLOWED_HOSTS:
            return redirect(url)
        else:
            return redirect(url_for('error_redirect'))

@app.route('/error_redirect')
def error_redirect():
    return "Invalid url. The host of redirection is not on the allowed hosts."

if __name__ == '__main__':
    app.run()