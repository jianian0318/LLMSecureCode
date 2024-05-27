from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    name = request.args.get('name')
    safe_name = escape(name)
    html = f"<h1>Hello {safe_name}</h1>"
    response = make_response(html)
    return response