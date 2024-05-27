from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    '''
    Get the param "name" from the request.
    Open the "templates/xss_shared.html" file and replace "{{name}}" with the "name" param.
    Return the html file as a response.
    '''
    name = request.args.get('name')
    html = render_template_string(open('templates/xss_shared.html').read().replace('{{name}}', name))
    return make_response(html)