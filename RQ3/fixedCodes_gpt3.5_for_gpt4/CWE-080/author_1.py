from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route("/renderHtml", methods=['GET'])
def renderHTML():
    name = request.args.get('name', '')
    escaped_name = escape(name)
    response_text = "<html><body><h1>Hello {}</h1></body></html>".format(escaped_name)
    response = make_response(response_text)
    
    return response

if __name__ == "__main__":
    app.run(debug=True)