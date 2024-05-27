from flask import request, Response, Flask, redirect, safe_join, urlparse

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')
    if next_url:
        parsed_url = urlparse(next_url)
        if parsed_url.scheme and parsed_url.netloc:
            return Response('Invalid URL', 400)
        else:
            return redirect(safe_join(request.url_root, next_url))
    else:
        return Response('Missing "next" parameter', 400)

if __name__ == '__main__':
    app.run()