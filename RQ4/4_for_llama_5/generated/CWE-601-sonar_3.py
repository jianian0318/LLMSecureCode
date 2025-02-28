from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    next_url = request.args.get('next')
    response = Response(status=302)
    response.headers['Location'] = next_url
    return response

if __name__ == '__main__':
    app.run(debug=False)