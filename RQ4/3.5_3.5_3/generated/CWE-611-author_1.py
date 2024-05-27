import defusedxml.lxml as lxml

@app.route("/upload", methods=["POST"])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    # Retrieve the xml file from the request
    xml_file = request.files.get('xml_file')

    # Parse the xml file using defusedxml
    xml_data = lxml.parse(xml_file)

    # Extract the userid and password from the xml data
    userid = xml_data.findtext('userid')
    password = xml_data.findtext('password')

    # Check if the userid and password are correct
    if checkPassword(userid, password):
        return "Valid userid and password"
    else:
        return "Invalid userid or password"
