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
    name = request.args.get('name')
    
    # 创建一个 jinja2 Environment
    env = Environment(loader=FileSystemLoader('/path/to/templates/'))
    
    # 从环境中获取 template.html 并渲染
    template = env.get_template('template.html')
    rendered_template = template.render(name=name)
    
    return rendered_template
