from flask import Flask, request, make_response
from html import escape

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    name_param = request.args.get('name', None)
    if name_param is None:
        response = make_response("No name provided", 400)
    else:
        escaped_name = escape(name_param)
        response = make_response(f"Name is: {escaped_name}", 200)
    return response

if __name__ == "__main__":
    app.run(debug=True)