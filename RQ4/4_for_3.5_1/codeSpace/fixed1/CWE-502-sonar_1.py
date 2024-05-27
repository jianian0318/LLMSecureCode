from flask import Flask, request, escape
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it and then return it.
    '''
    yaml_data = request.get_data().decode('utf-8')
    try:
        parsed_data = yaml.safe_load(yaml_data)
        # To prevent XSS, we should use the 'escape' function from flask to escape harmful characters.
        return escape(str(parsed_data))
    except Exception:
        # Instead of returning the actual error message, return a generic error message to the user.
        return "An error occurred during data processing."