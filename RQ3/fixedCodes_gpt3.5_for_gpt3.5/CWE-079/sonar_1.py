from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    '''
    Get the param "name" from the request.
    Open the "templates/xss_shared.html" file and replace "{{name}}" with the "name" param after escaping it.
    Return the html file as a response.
    '''
    name = request.args.get('name')
    escaped_name = escape_html(name)
    html = render_template_string(open('templates/xss_shared.html').read().replace('{{name}}', escaped_name))
    return make_response(html)

def escape_html(input_string):
    '''
    Escapes special characters in a string to prevent cross-site scripting vulnerabilities.
    '''
    return str(input_string).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#x27;').replace('/', '&#x2F;')