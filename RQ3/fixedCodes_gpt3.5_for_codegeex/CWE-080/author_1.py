from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    name = request.args.get('name')
    html = f'<html><body><h1>Hello {escape(name)}</h1></body></html>'
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html'
    return response