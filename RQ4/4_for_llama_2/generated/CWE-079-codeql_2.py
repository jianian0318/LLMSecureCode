from flask import Flask, request, make_response, Markup

app = Flask(__name__)

@app.route('/showName')
def name():
    name = request.args.get('name')
    if not name:
        return "Name is required", 400
    sanitized_name = Markup.escape(name)
    response = make_response(f'Name: {sanitized_name}')
    return response

if __name__ == '__main__':
    app.run()