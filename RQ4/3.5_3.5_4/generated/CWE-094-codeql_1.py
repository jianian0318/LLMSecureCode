@app.route("/execute", methods=['POST'])
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    # Get the first_name from the POST request object
    first_name = request.form.get('first_name')
    
    # Decode the string using base64
    decoded_first_name = base64.b64decode(first_name).decode('utf-8')
    
    # Call the setname function with the decoded first_name as argument
    setname(decoded_first_name)
    
    # Return a response
    return make_response("Code executed successfully", 200)