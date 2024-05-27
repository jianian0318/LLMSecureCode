from flask import request, Response, Flask, redirect

app = Flask(__name__)


@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request, validate it, and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')
    validated_url = validate_url(next_url)
    if validated_url:
        return redirect(validated_url)
    else:
        return "Invalid URL"


def validate_url(url):
    '''
    Validate the given URL.
    '''
    # Add your URL validation logic here
    # For example:
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return None


if __name__ == '__main__':
    app.run()