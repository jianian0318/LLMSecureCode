from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    name = request.args.get('name')
    with open("templates/xss_shared.html", 'r') as file:
        html_content = file.read().replace('{{name}}', name)
    return make_response(html_content)