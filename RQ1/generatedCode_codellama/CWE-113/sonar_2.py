from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def route():
    content_type = request.args.get('content_type')
    response = Response(content_type=content_type)
    return response

if __name__ == '__main__':
    app.run()
