from flask import Flask, request, Response, redirect

app = Flask(__name__)

@app.route('/')
def route():
    content_type = request.args.get('content_type')
    if content_type is not None:
        content_type = content_type.replace('\r', '').replace('\n', '')
    else:
        content_type = 'text/html'
    response = Response(content_type=content_type)
    return response

if __name__ == '__main__':
    app.run()