from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
from markupsafe import escape

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    # Use "escape" from the markupsafe package to sanitize the user input
    name = escape(request.args.get('name'))
    
    env = Environment(loader=FileSystemLoader('/path/to/templates'))

    template = env.get_template('template.html')
    
    return template.render(name=name)

if __name__ == "__main__":
    app.run(debug=True)


