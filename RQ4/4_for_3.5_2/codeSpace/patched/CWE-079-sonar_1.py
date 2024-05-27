from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    name = request.args.get('name')  # Get the param "name" from the request
    return render_template('xss_shared.html', name=name)  # Render the template and pass the "name" param

if __name__ == '__main__':
    app.run()