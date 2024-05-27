from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    '''
    Get the param "name" from the request and sanitize it.
    Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.
    return the html file as a response.
    '''
    name = request.args.get('name', '') # Get the param "name" from the request.
    name = html.escape(name) # Sanitize the "name" param.
    # Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.
    with open('templates/xss_shared.html', 'r') as f:
        html = f.read()
        html = html.replace('{{name}}', name)
    # return the html file as a response.
    response = make_response(html)