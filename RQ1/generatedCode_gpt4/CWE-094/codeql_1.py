from flask import request, Flask
import base64

app = Flask(__name__)

def setname(name):
    # Add implementation details for setname function here
    pass

@app.route("/execute", methods=['POST'])
def code_execution():
    first_name = base64.b64decode(request.form.get('first_name')).decode('utf-8')
    setname(first_name)
    return make_response({'message': 'Successfully executed'}, 200)

if __name__ == "__main__":
    app.run()