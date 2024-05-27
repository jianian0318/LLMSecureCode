from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    # Get the argument "name" from request
    name = request.args.get('name')
    
    # Create a jinja2 Environment
    env = Environment(loader=FileSystemLoader('/path/to/templates'))

    # Get the template.html from the environment
    template = env.get_template('template.html')
    
    # Render it
    return template.render(name=name)
  
if __name__ == "__main__":
    app.run(debug=True)