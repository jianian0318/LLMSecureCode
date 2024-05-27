from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    # Get the argument "name" from the request
    name = request.args.get('name')

    # Create a jinja2 Environment with autoescaping
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    # Get the template.html from the environment
    template = env.get_template('template.html')
    
    # Render the template with the given name
    output = template.render(name=name)
    
    return output