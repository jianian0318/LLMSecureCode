from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/set_location_header', methods=['GET', 'POST'])
def set_location_header():
    # Get the "next" value from the request arguments
    next_url = request.args.get('next', None)
    if not next_url:
        # If no "next" value is provided, it won't redirect
        return Response("No next_url provided.", status=400)
    else:
        # Create a response and set the location header for redirecting to the value of "next"
        response = Response("Redirecting...", status=302)
        response.headers['Location'] = next_url
        return response