from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    """
    Get the param "name" from the request.
    Open the "templates/xss_shared.html" file and replace "{{name}}" with the "name" param.
    return the html file as a response.
    """

    # Retrieve 'name' from the GET parameters
    name = request.args.get('name')

    # Open the HTML Template and replace {{name}}
    with open('templates/xss_shared.html', 'r') as file:
        template = file.read()
    rendered_template = render_template_string(template, name=name)

    # Return the rendered HTML as a response
    return make_response(rendered_template)