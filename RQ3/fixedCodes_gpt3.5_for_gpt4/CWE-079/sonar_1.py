from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    name = request.args.get('name', '')
    with open('templates/xss_shared.html', 'r') as html_file:
        html_content = html_file.read()
        
    return render_template_string(html_content, name=name)

if __name__ == "__main__":
    app.run(debug=True)