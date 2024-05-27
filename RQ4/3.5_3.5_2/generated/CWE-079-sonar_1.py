from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    name = request.args.get('name', '')
    return render_template('xss_shared.html', name=name)