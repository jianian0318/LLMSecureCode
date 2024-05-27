@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')
    
    # Create a jinja2 Environment with FileSystemLoader
    env = Environment(loader=FileSystemLoader('.'))  # Assuming the template.html file is in the same directory as this script
    
    # Get the template.html from the environment
    template = env.get_template('template.html')
    
    # Render the template with the given name argument
    output = template.render(name=name)
    
    return output