from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['GET', 'POST'])
def yaml_load():
    if request.method == 'POST':
        # Get YAML data from request
        yaml_data = request.get_data(as_text=True)
        
        try:
            # Parse the YAML data
            parsed_data = yaml.safe_load(yaml_data)
            
            # Return the parsed YAML data
            return parsed_data
            
        except yaml.YAMLError as e:
            # Error handling for invalid YAML data
            return f"Invalid YAML data: {e}"
            
    else:
        # Return an empty response if the method is not POST
        return ''