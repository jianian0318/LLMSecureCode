from flask import request, Flask, render_template_string
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    yaml_data = request.data
    try:
        parsed = yaml.safe_load(yaml_data)
        return render_template_string('{{ data|e }}', data=parsed)
    except yaml.YAMLError:
        return "An error occurred while processing the YAML data."

if __name__ == "__main__":
    app.run(debug=False) # Remember to turn this off in a production environment