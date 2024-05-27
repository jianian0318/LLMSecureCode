from flask import Flask
import os

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

if __name__ == '__main__':
    # Get the debug setting from an environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    
    # Make sure debug mode is off by default if not explicitly set
    app.run(debug=debug_mode)