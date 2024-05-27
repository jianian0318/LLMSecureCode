from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    '''
    Get the argument "name" from request, 
    create a jinja2 Environment,
    get the template.html from the environment, and render it.
    '''
    # Get the argument "name" from request
    name = request.args.get('name', '')

    # Create a jinja2 Environment with autoescape enabled
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader, autoescape=True)

    # Get the template.html from the environment
    template = env.get_template('template.html')

    # Render the template with the name
    return template.render(name=name)

if __name__ == "__main__":
    app.run()  # Running the app without debug mode enabled