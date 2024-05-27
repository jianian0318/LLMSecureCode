from flask import request, redirect, Flask

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    """
    Get the url from the request and redirect to it
    """
    url = request.args.get('url', default = None, type = str)
    if url is not None:
        return redirect(url)
    else:
        return "No URL parameter provided for redirection."

if __name__ == '__main__':
    app.run()