from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/set_location_header')
def set_location_header():
    next_value = request.args.get('next')
    response = Response()
    response.headers['Location'] = next_value
    return response


if __name__ == '__main__':
    app.run()