from flask import request, Flask
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    if request.data:
        data = request.data.decode("utf-8")
        try:
            yml_data = yaml.safe_load(data)
        except yaml.YAMLError as e:
            return {'error': 'Invalid YAML data', 'details': str(e)}, 400
        else:
            ### Replace ... with your processing or direct return statement
            ...

            return {'success': True, 'data': yml_data}, 200
    else:
        return {'error': 'No data provided'}, 400

if __name__ == "__main__":
    app.run()