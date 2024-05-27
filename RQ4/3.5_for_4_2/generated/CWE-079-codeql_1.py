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
    name = request.args.get('name', '')  # Get the argument "name" from request

    # Create a jinja2 Environment with autoescape=True
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader, autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('template.html')  # Get the template.html from the environment

    return template.render(name=name)  # render it