from flask import Flask, request
import traceback
import ast

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    """
    Get the user input from the request,
    compile it into a python code, then execute it.
    """
    user_code = request.get_json()["code"]
    try:
        output = ast.literal_eval(user_code)
        return {"output": output}, 200
    except Exception as e:
        return {"error": str(traceback.format_exc())}, 400

if __name__ == "__main__":
    app.run(debug=False)