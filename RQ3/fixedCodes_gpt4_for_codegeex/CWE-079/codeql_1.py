from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    '''
    Get the argument "name" from request, 
    create a jinja2 Environment,
    get the template.html from the environment, and render it.
    '''
    name = request.args.get('name')

    # Create a jinja2 Environment
    env = Environment(loader=FileSystemLoader('/path/to/templates/'),
                      autoescape=select_autoescape(['html']))

    # Get template.html from the environment and render it
    template = env.get_template('template.html')
    rendered_template = template.render(name=name)

    return rendered_template