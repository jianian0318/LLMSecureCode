import urllib

@app.route('/')
def index():
    version = request.args.get('version')
    version = version.replace("__", "")
    version = version.replace("globals", "")
    version = version.replace("locals", "")
    version = version.replace("object", "")
    version = version.replace("open", "")
    version = version.replace("exec", "")
    version = version.replace("compile", "")
    version = version.replace("eval", "")
    version = version.replace("input", "")
    version = version.replace("help", "")
    version = version.replace("dir", "")
    version = version.replace("type", "")
    version = version.replace("etc", "")
    version = version.replace("sys", "")
    version = version.replace("exit", "")
  
    return 'Module version: ' + urllib.__version__