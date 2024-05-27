from flask import Flask, request, escape
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=["POST"])
def yaml_load():
    # Get YAML data from request
    yaml_data = request.data.decode()

    try:
        # Use safe_load instead of load
        parsed_data = yaml.safe_load(yaml_data)
    except yaml.YAMLError:
        return "Invalid YAML format", 400

    # Use escape to avoid cross-site scripting vulnerability
    return escape(str(parsed_data))

if __name__ == '__main__':
    app.run()