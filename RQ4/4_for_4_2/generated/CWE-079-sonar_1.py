from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    # Get the param "name" from the request and sanitize it
    name = escape(request.args.get('name', '', type=str))
    
    # Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.
    with open('templates/xss_shared.html', 'r') as file:
        file_contents = file.read()   
        
    html_content = file_contents.replace("{{name}}", name)
        
    # return the html file as a response.
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response