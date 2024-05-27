from flask import Flask, request, make_response
from jinja2 import escape

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    name = request.args.get('name', '')
    name = escape(name)
    with open('templates/xss_shared.html', 'r') as html_file:
        html_content = html_file.read().replace("{{name}}", name)
        
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == "__main__":
    app.run(debug=True)