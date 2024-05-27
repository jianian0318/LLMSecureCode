def setname(name):
    # implementation of setname function

@app.route("/execute", methods=['POST'])
def code_execution():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        decoded_name = base64.b64decode(first_name).decode('utf-8')
        setname(decoded_name)
        return make_response("Code executed successfully", 200)
    else:
        return make_response("Invalid request method", 405)