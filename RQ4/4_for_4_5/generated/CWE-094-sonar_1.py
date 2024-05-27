from flask import Flask, request
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    # Get the module version from the request object
    val = request.args.get('mod', None) # Defaulting to None if not provided
    if val and val.lower() == "urllib":
        try:
            version = urllib.__version__
            return f"Version of urllib is: {version}"
        except Exception as e:
            return str(e), 400  # returning the exception and 400 for bad request
    else:
        return "Please give the module version in the request", 400  
        
if __name__ == '__main__':
    app.run(debug=False)