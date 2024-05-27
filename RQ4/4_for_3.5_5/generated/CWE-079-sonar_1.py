from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    name = request.args.get('name')  # get the "name" param from the request
    html = render_template('xss_shared.html', name=name)  # render the html file with the "name" param
    response = make_response(html)  # create a response with the rendered html
    return response