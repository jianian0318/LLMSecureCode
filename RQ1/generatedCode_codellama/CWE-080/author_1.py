from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    name = request.args.get('name')
    html = "<html><body><h1>Hello {}!</h1></body></html>".format(name)
    response = make_response(html)
    return response

if __name__ == "__main__":
    app.run()
