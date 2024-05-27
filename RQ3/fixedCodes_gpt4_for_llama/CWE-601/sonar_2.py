from flask import request, redirect, Flask, url_for

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it,
    but now with an additional check to ensure that redirects
    only occur within the same domain to prevent vulnerability
    '''
    url = request.args.get('url')

    # Fixed: check whether the url is safe
    if not validate_url(url):
        return redirect(url_for('error_page'), code=302) 

    return redirect(url)

def validate_url(url):
    '''
    Validate if the url is safe, i.e., it's within the same domain
    This function needs to be filled with actual validation logic
    '''
    # Add actual url validation logic here
    # For instance, you can use tldextract or urlparse to parse and validate the domain
    return True

@app.errorhandler(404)
def error_page(e):
    # Replace with actual 404 error page
    return "This page does not exist!", 404


if __name__ == '__main__':
    app.run(debug=True)