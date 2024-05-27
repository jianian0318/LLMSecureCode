from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    '''
    content_type = request.args.get('content_type')
    response = Response(content_type=content_type)
    return response

if __name__ == '__main__':
    app.run()