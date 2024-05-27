from flask import request, Flask, make_response
import base64

app = Flask(__name__)

def setname(name):
    # Add implementation details for setname function here
    pass

@app.route("/execute", methods=['POST'])
def code_execution():
    try:
        first_name = base64.b64decode(request.form.get('first_name')).decode('utf-8')
        if (first_name is not None and len(first_name)>0):
            setname(first_name)
            return make_response({'message': 'Successfully executed'}, 200)
        else:
            return make_response({'message': 'Error in processing request. Parameter missing.'}, 400)
    except Exception as e:
        return make_response({'message': 'Error in processing request. Details: '+str(e)}, 500)

if __name__ == "__main__":
    app.run()