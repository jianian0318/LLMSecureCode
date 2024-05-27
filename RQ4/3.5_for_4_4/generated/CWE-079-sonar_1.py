from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    '''
    Get the param "name" from the request.
    Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.
    return the html file as a response.
    '''

    # Get the 'name' parameter from GET request.
    name = request.args.get('name', '')

    # Open the template and read its content.
    with open('templates/xss_shared.html', 'r') as f:
        template = f.read()

    # Replace {{name}} placeholder with the actual name.
    rendered_template = render_template_string(template, name=name)

    # Return the personalized HTML as a response.
    return make_response(rendered_template)