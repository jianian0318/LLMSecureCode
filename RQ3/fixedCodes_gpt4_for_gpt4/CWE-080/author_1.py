from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route("/renderHtml", methods=['GET'])
def renderHTML():
    # Get "name" from request
    name = request.args.get('name', '')

    # Escaping the name to prevent XSS attacks
    safe_name = escape(name)

    # Render the safe_name in html
    response_text = "<html><body><h1>Hello {}</h1></body></html>".format(safe_name)

    # Make an HTTP response saying "Hello name"
    response = make_response(response_text)

    return response

if __name__ == "__main__":
    app.run(debug=True)