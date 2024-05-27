from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    # Get the argument "name" from request
    name = request.args.get('name', 'default name')

    # Create a jinja2 Environment and set the loader to FileSystemLoader
    # Enable autoescaping for HTML files to prevent XSS attacks
    env = Environment(loader=FileSystemLoader('templates'), autoescape=select_autoescape(['html', 'xml']))

    # Get the template.html from the environment
    template = env.get_template('template.html')

    # Render the template with the passed arguments
    rendered_template = template.render(name=name)

    return rendered_template

if __name__ == '__main__':
    # Ensure to set debug=False in production to avoid vulnerabilities
    app.run(debug=False)