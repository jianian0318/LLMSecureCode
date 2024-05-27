from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape
app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    '''
    Get the argument "name" from request, 
    create a jinja2 Environment with autoescape enabled,
    get the template.html from the environment, and render it.
    '''
    # Get argument "name" from request
    name = request.args.get('name')
    
    # Create a Jinja2 Environment, and enable autoescape.
    env = Environment(
        loader=FileSystemLoader('/path/to/templates/folder'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    # Get the template.html from the environment
    template = env.get_template('template.html')

    # Render it
    return template.render(name=name)

if __name__ == "__main__":
    app.run(debug=False)