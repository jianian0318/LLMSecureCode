from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    # Get the param "name" from the request.
    name = request.args.get('name',"")
    
    # Escape special characters to prevent cross-site scripting vulnerability.
    name = escape(name)
  
    # Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.   
    with open("templates/xss_shared.html", "r") as file:
        html = file.read().replace("{{name}}", name)
        
    # Return the html file as a response.
    response = make_response(html)
    response.headers["Content-Type"] = "text/html"
    
    return response

if __name__ == '__main__':
    app.run() # Remove debug=True to prevent exposing the Werkzeug debugger and allowing arbitrary code execution.