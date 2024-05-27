from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName')
def name():
    name = request.args.get('name')
    if not name:
        return "Please provide a name"
    safe_name = escape(name)  # Escape potentially harmful characters for safe rendering in HTML
    response = make_response(safe_name)
    return response

if __name__ == '__main__':
    app.run()