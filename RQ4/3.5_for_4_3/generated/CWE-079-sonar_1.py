from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    name = escape(request.args.get('name'))  # get the param "name" from the request and escape any HTML characters
    with open('templates/xss_shared.html', 'r') as file:
        file_data = file.read()
        file_data = file_data.replace('{{name}}', name)  # replace "{{name}}" with the "name" param
    response = make_response(file_data)  # add the html file into response
    response.mimetype = "text/html"  # specify the mime type
    return response  # return the html file as a response

if __name__ == "__main__":
    app.run()