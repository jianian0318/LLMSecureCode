from flask import Flask, request
import importlib

app = Flask(__name__)

@app.route('/')
def index():
    version = request.args.get('version')
    module_name = f"urllib{version}"
    try:
        importlib.import_module(module_name)
        return f"Imported {module_name}"
    except ModuleNotFoundError:
        return "Module not found"

if __name__ == '__main__':
    app.run()