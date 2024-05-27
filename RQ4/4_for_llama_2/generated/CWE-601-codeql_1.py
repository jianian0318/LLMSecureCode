from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def redirect():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url')
    return redirect(url_for(next_url), code=302)


if __name__ == '__main__':
    app.run()