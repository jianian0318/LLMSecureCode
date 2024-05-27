@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_data = request.data
    root = ET.fromstring(xml_data)
    return root