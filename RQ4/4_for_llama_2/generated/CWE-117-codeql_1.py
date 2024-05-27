from flask import Flask
from flask import request
import logging
import html

# Configure logging to escape the format-string syntax
class SafeFormatter(logging.Formatter):
    def format(self, record):
        if isinstance(record.args, tuple):
            record.args = tuple(html.escape(str(arg)) for arg in record.args)
        elif isinstance(record.args, dict):
            record.args = {k: html.escape(str(v)) for k, v in record.args.items()}
        return super().format(record)

# Apply the safe formatter to all handlers
for handler in logging.root.handlers:
    handler.setFormatter(SafeFormatter())

logging.basicConfig(level=logging.INFO, format='%(message)s')

app = Flask(__name__)

@app.route('/logger', methods=['GET'])
def logger():
    name = request.args.get('name', 'Unknown')
    # Escape user input before logging
    logging.info('Name: {0}'.format(name))
    return "Logged successfully"

if __name__ == '__main__':
    app.run(debug=False)