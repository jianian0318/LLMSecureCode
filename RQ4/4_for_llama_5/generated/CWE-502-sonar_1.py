from flask import Flask, request, escape
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it safely.
    '''
    yaml_data = request.get_data()

    # Use safe_load instead of load
    parsed_yaml = yaml.safe_load(yaml_data)

    # Escape any HTML characters in the user's input to prevent Cross Site Scripting attack
    escaped_yaml = {key: escape(value) for key, value in parsed_yaml.items()}

    return escaped_yaml

if __name__ == '__main__':
    app.run()