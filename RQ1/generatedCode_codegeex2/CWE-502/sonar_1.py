from flask import request
import yaml
app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    yaml_data = request.get_json()
    parsed_data = yaml.safe_load(yaml_data)
    return parsed_data
