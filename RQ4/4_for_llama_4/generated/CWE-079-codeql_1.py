from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])  # autoescape set to True for '.html' and '.xml' files
    )
    template = env.get_template('template.html')
    rendered_template = template.render(name=name)
    return rendered_template

if __name__ == '__main__':
    app.run()