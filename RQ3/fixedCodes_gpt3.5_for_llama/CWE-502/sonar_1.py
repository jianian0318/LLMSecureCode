from flask import request, Flask
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    if request.method == 'POST':
        yaml_data = request.get_data()
        try:
            data = yaml.safe_load(yaml_data)
            return data
        except yaml.YAMLError as exc:
            return "Error: Invalid YAML data", 400

if __name__ == '__main__':
    app.run()