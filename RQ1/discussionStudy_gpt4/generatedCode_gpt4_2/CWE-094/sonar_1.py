from flask import Flask, request
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    module_version = urllib.__version__
    exec("import urllib{}".format(module_version))
    return "Module Imported Successfully"

if __name__ == "__main__":
    app.run(debug=True)