from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def route():
    content_type = request.args.get('content_type')
    
    if content_type is not None and '/' not in content_type:
        response = Response("Response with content type: " + content_type, content_type=content_type)
    else:
        response = Response("Invalid content type", content_type='text/plain')

    return response

if __name__ == "__main__":
    app.run(debug=True)