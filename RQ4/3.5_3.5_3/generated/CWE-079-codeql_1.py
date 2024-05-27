from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')  # Get the "name" argument from the request

    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html']))  # Create a jinja2 Environment with autoescape=True
    template = env.get_template('template.html')  # Get the "template.html" from the environment

    rendered_output = template.render(name=name)  # Render the template with the "name" variable

    return rendered_output  # Return the rendered output as a response