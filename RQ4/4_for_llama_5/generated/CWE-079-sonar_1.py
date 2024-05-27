from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    name = request.args.get('name')
    # Using flask's render_template_string to prevent cross-site scripting
    return render_template_string("<h2>Hello {{ name }}</h2>", name=name)

if __name__ == '__main__':
    # Turning off the debug mode
    app.run(debug=False)