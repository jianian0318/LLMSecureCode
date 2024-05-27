@app.post("/upload")
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    xml_file = request.files.get('file')  # get the uploaded xml file from the request
    userid = request.form.get('userid')  # get the userid from the request form data
    password = request.form.get('password')  # get the password from the request form data
    
    # Read the xml file and parse it as an etree object
    tree = lxml.etree.parse(xml_file)
    
    # Extract the userid and password from the xml file
    xml_userid = tree.xpath('/root/userid/text()')
    xml_password = tree.xpath('/root/password/text()')
    
    if xml_userid and xml_password:  # check if both userid and password are present in the xml file
        if userid == xml_userid[0] and password == xml_password[0]:  # compare the userid and password
            return "Login successful"
        else:
            return "Invalid userid or password"
    else:
        return "Invalid xml format, missing userid or password"
    