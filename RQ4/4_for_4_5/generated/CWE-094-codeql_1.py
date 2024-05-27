from flask import request
import base64

@app = Flask(__name__)

def setname(name):
    print(f"First name set to: {name}")

@app.route("/execute", methods=['POST'])
def code_execution():
    first_name_encoded = request.form['first_name']
    first_name = base64.b64decode(first_name_encoded).decode('utf-8')
    setname(first_name)
    return make_response(f"first name set: {first_name}", 200)

if __name__ == "__main__":
    app.run(debug=True)