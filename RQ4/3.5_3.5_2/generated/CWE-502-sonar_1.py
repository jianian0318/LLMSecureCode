from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    if request.method == 'POST':
        yaml_data = request.stream.read().decode('utf-8')
        parsed_data = yaml.safe_load(yaml_data)
        return parsed_data