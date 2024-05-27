from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name')
    return render_template('template.html', name=name)

if __name__ == '__main__':
    app.run()