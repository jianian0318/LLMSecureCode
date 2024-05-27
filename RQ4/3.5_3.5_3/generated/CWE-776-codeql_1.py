@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    # Get the XML data from the request
    xml_data = request.data
    
    # Parse the XML data using ElementTree
    root = ET.fromstring(xml_data)
    
    # Perform any necessary operations on the parsed XML
    
    # Return the processed XML
    return ET.tostring(root)