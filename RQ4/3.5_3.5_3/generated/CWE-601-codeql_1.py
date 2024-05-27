from flask import Flask, redirect, request, abort
from urllib.parse import urlparse, urljoin
import re

app = Flask(__name__)

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url')
    if next_url:
        # Validate the next_url input
        parsed_url = urlparse(next_url)
        if parsed_url.scheme and parsed_url.netloc:
            # Validate the next_url using regex
            if re.match('^[a-zA-Z0-9-]+$', parsed_url.path):
                full_url = urljoin(request.url_root, next_url)
                if parsed_url.netloc == request.host:
                    return redirect(full_url)
                else:
                    abort(400)
            else:
                abort(400)
        else:
            abort(400)
    else:
        return 'No next_url specified.'

if __name__ == '__main__':
    app.run()