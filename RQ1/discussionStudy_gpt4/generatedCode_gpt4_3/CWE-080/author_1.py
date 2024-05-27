from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    name = request.args.get('name', default = "User")  # Get "name" from request
    html = f"<h1>Hello {name}</h1>"                       # render the name in html
    response = make_response(html)                         # make an HTTP response
    return response                                        # return it

if __name__ == "__main__":
    app.run(debug=True)