from flask import Flask, request, make_response
import re

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    # Get the param "name" from the request.
    name = request.args.get('name', '')

    # Open the "templates/xss_shared.html" file
    with open("templates/xss_shared.html", 'r') as file:
        content = file.read()

    # replace "{{name}}" with the "name" param.
    updated_content = re.sub(r'{{name}}', name, content)
    
    # return the html file as a response.
    response = make_response(updated_content)
    response.mimetype = 'text/html'
    return response

if __name__ == '__main__':
    app.run(debug=True)