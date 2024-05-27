from flask import request, Flask, escape
import yaml

app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    try:
        # use safe_load instead of load
        yaml_data = yaml.safe_load(request.data)
        
        # In a real application, additional steps might be required to securely
        # handle the YAML data, depending on what you are doing with it. If you
        # are returning it to a web page, ensure that you escape or encode it
        # properly to prevent XSS attacks.
        
        # Assuming we are escaping the output for display in an HTML context
        escaped_yaml_data = escape(yaml_data)

        return str(escaped_yaml_data)
    except yaml.YAMLError as exc:
        return "Error: Invalid YAML data", 400

if __name__ == "__main__":
   app.run()