from flask import request, redirect, Flask, abort
import validators

app = Flask(__name__)

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the url from the request and redirect to it after validating it.
    '''
    url = request.args.get('url')

    if validators.url(url):  # Validating the URL using validators library
        return redirect(validators.escape(url), code=302)  # Escaping the URL before redirecting
    else:
        abort(400) # Return an error if the URL is not valid

if __name__ == '__main__':
    app.run()