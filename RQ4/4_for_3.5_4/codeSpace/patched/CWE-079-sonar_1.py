from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    name = request.args.get('name') # Get the param "name" from the request

    # Open the "templates/xss_shared.html" file and replace "{{name}}" with the "name" param
    html_file = render_template('xss_shared.html', name=name)

    return make_response(html_file) # Return the html file as a response