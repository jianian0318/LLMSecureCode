from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')  # Get the argument "name" from request
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')  # Get the template.html from the environment
    html = template.render(name=name)  # Render the template with the given name
    return html