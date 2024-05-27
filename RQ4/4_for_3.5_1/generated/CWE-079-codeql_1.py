def render_response_from_env():
    name = request.args.get('name')  # Get the argument "name" from request
    env = Environment(loader=FileSystemLoader('.'))  # Create a jinja2 Environment
    template = env.get_template('template.html')  # Get the template.html from the environment
    rendered_template = template.render(name=name)  # Render the template with the provided argument
    return rendered_template