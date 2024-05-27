import urllib

@app.route('/')
def index():
    module_version = urllib.__version__
    return f"The version of urllib module is {module_version}"