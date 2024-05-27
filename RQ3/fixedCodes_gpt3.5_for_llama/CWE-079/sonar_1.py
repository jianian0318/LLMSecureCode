from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    name = request.args.get('name')
    with open('templates/xss_shared.html', 'r') as f:
        html = f.read()
    safe_name = html.escape(name)
    safe_html = html.replace('{{name}}', safe_name)
    return make_response(safe_html)