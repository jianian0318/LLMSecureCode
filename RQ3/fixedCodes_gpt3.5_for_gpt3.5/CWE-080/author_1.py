from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    name = request.args.get('name')
    sanitized_name = html.escape(name)
    html = f"<h1>Hello {sanitized_name}</h1>"
    response = make_response(html)
    return response