from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    '''
    Get the param "name" from the request.
    Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.
    return the html file as a response.
    '''
    name = request.args.get('name')
    with open('templates/xss_shared.html', 'r') as f:
        html = f.read()
    html = html.replace('{{name}}', name)
    return make_response(html)
