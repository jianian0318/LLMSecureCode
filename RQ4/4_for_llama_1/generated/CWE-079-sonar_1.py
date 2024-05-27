from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    name = escape(request.args.get('name'))
    with open('templates/xss_shared.html', 'r') as f:
        html = f.read()
    html = html.replace('{{name}}', name)
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == '__main__':
    app.run()