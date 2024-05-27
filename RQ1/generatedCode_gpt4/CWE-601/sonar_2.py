from flask import request, redirect, Flask

app = Flask(__name__)

@app.route('/flask_redirect')  # You need to add a forward slash at the start of your route
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    redirect_url = request.args.get('url')  # Fetch the URL to redirect to from the request parameters
    return redirect(redirect_url)  # Redirect to the fetched URL

if __name__ == '__main__':
    app.run()