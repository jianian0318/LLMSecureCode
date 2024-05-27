from flask import Flask, request
from importlib import import_module
from markupsafe import escape
import logging

app = Flask(__name__)

@app.route('/')
def index():
    # get version from get parameters
    module_version = request.args.get('version')
    if module_version:
        # Escape the input to prevent cross-site scripting (XSS).
        # Note that 'escape' comes from 'markupsafe' which is a dependency of Jinja2/Flask and should be used over Jinja2 escape
        module_version = escape(module_version)
        # Ensuring the version only contains alphanumeric characters helps prevent code/log injection.
        if not module_version.isalnum():
            app.logger.warning('Invalid module version format received: %s', module_version)
            return "Invalid module version"
    else:
        module_version = ''  # Set default empty string if no version parameter is provided
    try:
        urllib_version = import_module(f"urllib.{module_version}" if module_version else "urllib")
        # Log with safe string-formatting to prevent log injection
        app.logger.info('User requested: %s', f"urllib.{escape(module_version)}" if module_version else "urllib")
        return f"Successfully imported {'urllib.' + escape(module_version) if module_version else 'urllib'}"
    except Exception as e:
        # Log with safe string-formatting to prevent log injection
        app.logger.error('Error importing module %s: %s', escape(f"urllib.{module_version}" if module_version else "urllib"), e)
        return "An error occurred."
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # Setup logging properly
    app.run(debug=False)