from flask import request, Flask, make_response
import base64

app = Flask(__name__)

def setname(name):
    # Add implementation details for setname function here
    pass

@app.route("/execute", methods=['POST'])
def code_execution():
    first_name = request.form.get('first_name')
    if first_name:
        first_name = base64.b64decode(first_name).decode('utf-8')
        setname(first_name)
        return make_response({'message': 'Successfully executed'}, 200)
    else:
        return make_response({'error': 'Invalid input'}, 400)

if __name__ == "__main__":
    app.run()