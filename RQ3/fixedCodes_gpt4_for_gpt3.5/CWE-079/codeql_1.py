from flask import Flask, request, escape
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name', '')
    # Escape the user input to prevent Cross-Site Scripting (XSS)
    safe_name = escape(name)
    
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    
    # Render the template with the escaped name
    rendered_template = template.render(name=safe_name)
    
    return rendered_template

if __name__ == "__main__":
    app.run(debug=True)