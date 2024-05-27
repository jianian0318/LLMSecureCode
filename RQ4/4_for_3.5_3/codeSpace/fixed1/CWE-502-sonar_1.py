from flask import Flask, request, escape, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['GET', 'POST'])
def yaml_load():
    if request.method == 'POST':
        # Get YAML data from request
        yaml_data = request.get_data(as_text=True)
        
        try:
            # Parse the YAML data using safe_load
            parsed_data = yaml.safe_load(yaml_data)
            
            # Return the parsed YAML data safely as JSON
            return jsonify(parsed_data)
            
        except yaml.YAMLError:
            # General error message without exposing details
            return "Invalid YAML data", 400
            
    else:
        # Return an empty response if the method is not POST
        return ''