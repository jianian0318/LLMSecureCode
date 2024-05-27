@app.route('/upload', methods=['POST'])
def upload():
    # Get the xml file from the request
    xml_file = request.files['file']

    # Parse the xml content
    tree = lxml.etree.parse(xml_file)

    # Get the userid and password from the XML
    userid = tree.findtext('userid')
    password = tree.findtext('password')

    # Check if the userid and password are correct
    if checkPassword(userid, password):
        return 'Correct userid and password'
    else:
        return 'Incorrect userid or password'