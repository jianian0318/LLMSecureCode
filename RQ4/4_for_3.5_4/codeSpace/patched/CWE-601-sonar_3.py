from flask import request, Response, Flask, redirect

app = Flask(__name__)


@app.route('/set_location_header', methods=['GET'])
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_link = request.args.get("next")
    if next_link:
        # Set the "Location" header to the value of "next"
        response = Response()
        response.headers["Location"] = next_link
        return response, 302
    else:
        # Handle the case where "next" is not provided in the request
        return "Missing 'next' parameter", 400


if __name__ == "__main__":
    app.run()