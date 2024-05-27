import defusedxml.ElementTree as ET

@app.route('/upload', methods=['POST'])
def upload():
    """
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    """

    # Get the xml file from the request
    file = request.files['file']

    # Check if the file is an XML file
    if file.filename.endswith('.xml'):
        # Read the xml file
        xml_data = file.read()
        
        # Parse the xml data
        xml_tree = ET.fromstring(xml_data)
        
        # Get the userid and password from the xml
        userid = xml_tree.find('userid').text
        password = xml_tree.find('password').text
        
        # Check if the userid and password are correct
        if checkPassword(userid, password):
            return "Access granted"  # Return access granted message
        else:
            return "Access denied"  # Return access denied message
    else:
        return "Invalid file type"  # Return error message for invalid file type