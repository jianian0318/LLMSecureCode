from flask import request, Response, Flask, redirect, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_safe_url(target):
    '''
    First, we ensure that the target URL starts with either http:// or https://, 
    and then check whether the provided URL is intending to redirect to the same site or to a different site.
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    Implement safety check to prevent open redirect vulnerability.
    '''
    next_url = request.args.get('next')
    if not next_url or not is_safe_url(next_url):
        return redirect(url_for('default_page')) # Replace with your default page
    response = Response()
    response.headers['Location'] = next_url
    return response

if __name__ == '__main__':
    app.run()