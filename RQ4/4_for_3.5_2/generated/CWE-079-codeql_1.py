from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')  # Get the argument "name" from request
    # Initialize environment with autoescape for html extensions to mitigate XSS vulnerabilities
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')  # Get the template.html from the environment
    html = template.render(name=name)  # Render the template with the given name
    return html