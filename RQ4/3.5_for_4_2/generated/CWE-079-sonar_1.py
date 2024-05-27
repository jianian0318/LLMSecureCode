from flask import Flask, request, make_response, render_template_string, escape
import os

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    # Get the param "name" from the request
    name = request.args.get('name')

    # Create a template file path
    template_path = os.path.join('templates', 'xss_shared.html')
    
    # Read the contents of the template file
    with open(template_path, 'r') as file:
        filedata = file.read()

    # Escape the "name" param to prevent cross-site scripting (XSS) attacks
    escaped_name = escape(name)

    # Render the template with the escaped name
    rendered_template = render_template_string(filedata, name=escaped_name)

    # Return the rendered template as a response.
    response = make_response(rendered_template)
    response.headers['Content-Type'] = 'text/html'

    return response