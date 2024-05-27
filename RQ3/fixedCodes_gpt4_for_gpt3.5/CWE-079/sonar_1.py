from flask import Flask, request, make_response, render_template_string, escape

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    '''
    Get the param "name" from the request.
    Sanitize/Escape the "name" param to prevent XSS attacks.
    Open the "templates/xss_shared.html" file and replace "{{name}}" with the "name" param.
    Return the html file as a response.
    '''
    name = request.args.get('name')
    sanitized_name = escape(name)
    html = render_template_string(open('templates/xss_shared.html').read().replace('{{name}}', sanitized_name))
    return make_response(html)