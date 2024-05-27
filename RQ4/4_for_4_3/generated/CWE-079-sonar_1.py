from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    # Get the param "name" from the request.
    name = request.args.get('name', '')
    
    # Open the "templates/xss_shared.html" file
    with open('templates/xss_shared.html', 'r') as f:
        template = f.read()
        
    # Replace  "{{name}}" with the "name" param.
    html = render_template_string(template, name=name)

    # Return the html file as a response.
    return html