from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')
    if next_url:
        if not next_url.startswith('http://') and not next_url.startswith('https://'):
            return Response(status=400, headers={'Location': '/error'})
        return Response(status=302, headers={'Location': next_url})
    else:
        return 'No "next" value provided.'