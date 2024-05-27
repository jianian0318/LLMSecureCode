from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def route():
    # Get the content_type parameter from the request
    content_type = request.args.get('content_type')
    
    # Create a response with the content_type
    response = Response("Response with content type: " + content_type, content_type=content_type)

    # Send it as a response
    return response

if __name__ == "__main__":
    app.run(debug=True)