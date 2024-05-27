from flask import Flask, request
import importlib

app = Flask(__name__)

@app.route('/')
def index():
    module_version = request.args.get('module_version')
    if not module_version:
        return "Error: module_version is required", 400

    try:
        module_name = 'urllib' + module_version
        importlib.import_module(module_name)
    except ImportError:
        return "Error: Invalid module version", 400

    return "Module version: " + module_version