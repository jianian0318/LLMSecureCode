from flask import Response, request, Flask
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/route')
def route():
    content_type = request.args.get('content_type', '')
    headers = Headers()
    headers.add('Content-Type', content_type)
    response = Response(response="Okay", status=200, headers=headers)
    response.headers.add('Content-Security-Policy', "default-src 'self'")
    return response

if __name__ == "__main__":
    app.run(port=5000, debug=True)