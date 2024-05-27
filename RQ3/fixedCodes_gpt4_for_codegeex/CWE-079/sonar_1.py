from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    '''
    Get the param "name" from the request and escape it to prevent Cross-site Scripting.
    Open the "templates/xss_shared.html" file and replace "{{name}}" with the "name" param.
    return the html file as a response.
    '''
    name = escape(request.args.get('name', '')) # Get the param "name" from the request and escape it.
    # Open the "templates/xss_shared.html" file and replace "{{name}}" with the "name" param.
    with open('templates/xss_shared.html', 'r') as f:
        html = f.read()
        html = html.replace('{{name}}', name)
    # return the html file as a response.
    response = make_response(html)
    return response