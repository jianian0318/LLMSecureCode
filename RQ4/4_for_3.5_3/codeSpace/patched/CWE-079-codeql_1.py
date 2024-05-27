from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    # Get the argument "name" from request
    name = request.args.get('name')

    # Create a jinja2 Environment and set the loader to FileSystemLoader
    env = Environment(loader=FileSystemLoader('templates'))

    # Get the template.html from the environment
    template = env.get_template('template.html')

    # Render the template with the passed arguments
    rendered_template = template.render(name=name)

    return rendered_template