from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get("name") # get the argument "name" from request
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml'])) # create a jinja2 Environment with autoescape enabled
    template = env.get_template('template.html') # get the template.html from the environment
    return template.render(name=name) # render the template and return the response