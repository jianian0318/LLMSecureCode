from flask import Flask, request, make_response
import os

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    name = request.args.get('name')  # Getting "name" parameter from the URL
    if not name:
        name = ""
        
    # Read the template file
    with open(os.path.join('templates', 'xss_shared.html'), 'r') as file:
        html_content = file.read()
    
    # Replace {{name}} with the name param
    html_content = html_content.replace("{{name}}", name)
    
    resp = make_response(html_content)
    resp.headers['Content-Type'] = 'text/html'
    
    return resp

if __name__ == "__main__":
    app.run()