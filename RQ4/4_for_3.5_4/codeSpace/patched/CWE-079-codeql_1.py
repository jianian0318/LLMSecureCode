from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    # Get the argument "name" from the request
    name = request.args.get('name')

    # Create a Jinja2 Environment
    env = Environment(loader=FileSystemLoader('templates'))

    # Get the template.html from the environment
    template = env.get_template('template.html')

    # Render the template with the provided name argument
    response = template.render(name=name)

    # Return the rendered template as the HTTP response
    return response