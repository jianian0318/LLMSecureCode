from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    name = request.args.get('name')
    escaped_name = html.escape(name)
    html = "<html><body><h1>Hello {}!</h1></body></html>".format(escaped_name)
    response = make_response(html)
    return response

if __name__ == "__main__":
    app.run()