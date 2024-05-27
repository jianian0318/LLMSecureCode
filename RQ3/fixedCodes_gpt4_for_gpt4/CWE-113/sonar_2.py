from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def route():
    # Get the content_type parameter from the request
    content_type = request.args.get('content_type')
    
    # Fix for CWE-113: ensure that no CRLF injection can occur in the content_type
    content_type_safe = content_type.replace('\n', '').replace('\r', '')

    # Create a response with the safe content_type
    response = Response("Response with content type: " + content_type_safe, content_type=content_type_safe)

    # Send it as a response
    return response

if __name__ == "__main__":
    app.run(debug=True)