from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name') # Get "name" from request

    # Create jinja2 Environment with autoescape enabled
    env = Environment(
        loader=FileSystemLoader('/path/to/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html') # Get template.html from the environment

    return template.render(name=name) # Render the template with the name