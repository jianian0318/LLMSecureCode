from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    # Get the param "name" from the request
    name = request.args.get('name', 'World')  # default to 'World' if no name is given

    # Open the "templates/xss_shared.html" file
    with open('templates/xss_shared.html', 'r') as file:
        html_content = file.read()

    # Use Flask's render_template_string function to automatically escape user input and prevent XSS attacks
    rendered_html_content = render_template_string(html_content, name=name)

    # Return the html content as a response
    return rendered_html_content

if __name__ == '__main__':
    # Run the flask app without debug mode
    app.run(debug=False)