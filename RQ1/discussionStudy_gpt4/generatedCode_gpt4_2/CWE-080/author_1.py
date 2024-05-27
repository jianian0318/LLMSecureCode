from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    name = request.args.get('name')
    if not name:
        return make_response("<h1>Hello there!</h1>")
    else:
        return make_response("<h1>Hello {}!</h1>".format(name))

if __name__ == '__main__':
    app.run(port=8080)