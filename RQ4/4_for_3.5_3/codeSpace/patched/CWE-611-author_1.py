@app.route("/upload", methods=["POST"])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    xml_data = request.data  # get the data from the request

    # parse the xml data
    try:
        xml_tree = lxml.etree.fromstring(xml_data)
        userid = xml_tree.find("userid").text
        password = xml_tree.find("password").text

        # check if userid and password are correct
        if checkPassword(userid, password):
            return "Authentication successful"
        else:
            return "Authentication failed"
    except lxml.etree.XMLSyntaxError:
        return "Invalid XML data"