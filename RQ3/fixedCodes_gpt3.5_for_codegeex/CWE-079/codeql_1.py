from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, escape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')
    
    # Create a jinja2 Environment
    env = Environment(loader=FileSystemLoader('/path/to/templates/'), autoescape=escape)
    
    # Get the template.html from the environment and render it
    template = env.get_template('template.html')
    
    # Render the template with the name parameter, ensuring automatic HTML escaping
    rendered_template = template.render(name=name)
    
    return rendered_template