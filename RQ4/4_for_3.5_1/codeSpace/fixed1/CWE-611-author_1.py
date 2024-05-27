from defusedxml import lxml

@app.post("/upload")
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    try:
        # Get the xml file from the request
        xml_file = request.files['file']
        
        # Load the xml tree
        tree = lxml.parse(xml_file)
        
        # Get the root element
        root = tree.getroot()
        
        # Get the userid and password from the xml
        userid = root.find('userid').text
        password = root.find('password').text
        
        # Check if the userid and password are correct
        if checkPassword(userid, password):
            return "Userid and Password are correct"
        else:
            return "Userid or Password are incorrect"
    
    except Exception as e:
        return str(e)