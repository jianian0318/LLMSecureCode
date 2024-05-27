from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName')
def name():
    # Get "name" from the request
    name = request.args.get('name', '')

    # Validate the name (for example, ensuring it's not empty)
    if not name:
        response = make_response("No name provided", 400)  # Bad Request
    else:
        # Sanitize the name to prevent cross-site scripting (XSS) vulnerabilities
        sanitized_name = escape(name)
        # Make a response with the sanitized name
        response = make_response(f'Hello, {sanitized_name}!', 200)  # OK

    # Return the response object
    return response

if __name__ == '__main__':
    app.run()