from flask import Response, request, Flask
from werkzeug.datastructures import Headers
from urllib.parse import quote

app = Flask(__name__)

@app.route('/route')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    '''
    content_type = request.args.get('content_type')
    safe_content_type = quote(content_type, safe='')
    response = Response(headers=Headers({'Content-Type': safe_content_type}))
    return response

if __name__ == '__main__':
    app.run()