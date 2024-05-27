from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    name = request.args.get('name')
    with open('templates/xss_shared.html', 'r') as f:
        html = f.read()
    response = make_response(render_template_string(html, name=name))
    return response

if __name__ == '__main__':
    app.run()