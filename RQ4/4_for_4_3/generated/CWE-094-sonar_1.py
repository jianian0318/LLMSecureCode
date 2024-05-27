from flask import Flask, request
import pkg_resources
import html

app = Flask(__name__)

@app.route('/<module_name>', methods=['GET'])
def get_module_version(module_name):
    """
    Return the version of the specified Python module
    """
    module_name = html.escape(module_name) # Escaping user input
    
    try:
        version = pkg_resources.get_distribution(module_name).version
    except pkg_resources.DistributionNotFound:
        version = f"No distribution found for {module_name}"
        
    return version

@app.route('/', methods=['GET'])
def get_flask_version():
    """
    Return the version of the Flask module
    """
    version = pkg_resources.get_distribution("Flask").version
    return version

if __name__ == '__main__':
    app.run()