from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    # Get the param "name" from the request
    name = request.args.get("name", default=None, type=str)
    # Render the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param
    rendered = render_template("xss_shared.html", name=name)
    # Return the html file as a response
    return make_response(rendered)