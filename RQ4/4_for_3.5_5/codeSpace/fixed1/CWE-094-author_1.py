from flask import Flask, request

app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def execute():
    """
    Get the user input from the request, check if it's a safe operation,
    and then safely execute it.
    """
    data = request.get_data(as_text=True)
    safe_operations = {'add', 'subtract'}

    if not data or data.split()[0].lower() not in safe_operations:
        return "Not allowed operation", 403

    result = handle_operation(data)
    return str(result)

def handle_operation(data):
    parts = data.split()
    operation = parts[0].lower()
    if operation == 'add':
        return int(parts[1]) + int(parts[2])
    elif operation == 'subtract':
        return int(parts[1]) - int(parts[2])

if __name__ == "__main__":
    app.run(debug=False) # Turn off debug mode for production