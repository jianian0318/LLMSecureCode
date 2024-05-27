from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')

    env = Environment(loader=FileSystemLoader('/path/to/templates'))

    template = env.get_template('template.html')

    # Fixed code to prevent Cross-site Scripting vulnerability
    safe_name = name.replace("<", "&lt;").replace(">", "&gt;")

    return template.render(name=safe_name)
  
if __name__ == "__main__":
    app.run(debug=True)