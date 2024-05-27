from flask import request
import yaml

app = Flask(__name__)


@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''        
    Get YAML data from request, parse it, and return it.        
    '''
    if request.method == 'POST':
        yaml_data = request.get_data()
        try:
            data = yaml.safe_load(yaml_data)
            return data
        except yaml.YAMLError as exc:
            return "Error: Invalid YAML data", 400