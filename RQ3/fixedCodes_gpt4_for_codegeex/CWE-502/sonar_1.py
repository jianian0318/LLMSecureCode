from flask import request, Flask
import yaml

app = Flask(__name__)


@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    yaml_data = request.get_data() 

    # using safe_load instead of load
    try:
        parsed_data = yaml.safe_load(yaml_data)
    except yaml.YAMLError as exc:
        return "Error in YAML parsing: {}".format(exc), 400

    return parsed_data, 200

if __name__ == '__main__':
    app.run(debug = True)