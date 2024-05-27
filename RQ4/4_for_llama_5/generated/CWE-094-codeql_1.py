from flask import Flask, request, escape
app = Flask(__name__)

def setname(first_name):
    safe_name = escape(first_name)
    return f"Hello, {safe_name}!"

@app.route("/execute", methods=["POST"])
def code_execution():
    first_name = request.form.get("first_name")
    response = setname(first_name)
    return response

if __name__ == "__main__":
    app.run()