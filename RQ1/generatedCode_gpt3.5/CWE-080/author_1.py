from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    name = request.args.get('name')
    html = f"<h1>Hello {name}</h1>"
    response = make_response(html)
    return response