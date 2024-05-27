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
    name = request.args.get('name')

    # File Loader
    file_loader = FileSystemLoader('templates')

    # create a jinja2 Environment
    env = Environment(loader=file_loader, autoescape=True)

    # get the tamplate from the environment
    template = env.get_template('template.html')

    # render the template and return
    output = template.render(name=name)
    return output

if __name__ == "__main__":
    app.run()