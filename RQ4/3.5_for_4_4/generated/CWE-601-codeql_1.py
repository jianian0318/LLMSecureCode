from flask import Flask, request, redirect, abort, urlparse

app = Flask(__name__)

@app.route('/')
def redirect_user():
    '''
    Redirects the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next', None)

    if next_url and urlparse(next_url).netloc == 'example.com':
        return redirect(next_url)
    else:
        return abort(400, "Invalid or missing parameter 'next'")