from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape, escape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    rendered_template = template.render(name=escape(name))
    return rendered_template