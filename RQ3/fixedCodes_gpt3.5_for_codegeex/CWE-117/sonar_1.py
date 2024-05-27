from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    input_data = request.args.get('input')
    
    sanitized_input = sanitize_input(input_data)
    
    current_app.logger.error(sanitized_input)
    
    return "Logged as an error"

def sanitize_input(input_data):
    return input_data.replace('\n', '').replace('\r', '')

if __name__ == "__main__":
    app.run()