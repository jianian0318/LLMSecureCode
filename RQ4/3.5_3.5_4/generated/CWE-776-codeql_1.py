@app.route("/upload", methods=["POST"])
def upload():
    '''
    Reads the XML from the incoming request.
    Parses it and returns it.
    '''
    # Get the XML data from the request
    xml_data = request.data
    
    # Parse the XML data
    root = ET.fromstring(xml_data)
    
    # Return the parsed XML
    return ET.tostring(root).decode()