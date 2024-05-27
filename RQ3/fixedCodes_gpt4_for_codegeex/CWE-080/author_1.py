from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    '''
    Get "name" from request,
    render the name in html, make an HTTP response saying "Hello name",
    and return it
    '''
    name = request.args.get('name')
    safe_name = escape(name)
    html = f'<html><body><h1>Hello {safe_name}</h1></body></html>'
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html'
    return response