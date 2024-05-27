def setname(name):
    # Function to set the name
    print("Setting name to:", name)

@app.route("/execute", methods=['POST'])
def code_execution():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        
        if first_name:
            decoded_name = base64.b64decode(first_name).decode('utf-8')
            setname(decoded_name)
            return make_response("Name set successfully", 200)
        else:
            return make_response("Missing 'first_name' in the request", 400)
    else:
        return make_response("Method not allowed", 405)

if __name__ == "__main__":
    app.run(debug=True)