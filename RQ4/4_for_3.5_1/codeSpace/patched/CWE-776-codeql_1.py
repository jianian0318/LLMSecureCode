@app.route("/upload", methods=["POST"])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_text = request.data
    root = ET.fromstring(xml_text)
    
    return ET.tostring(root)