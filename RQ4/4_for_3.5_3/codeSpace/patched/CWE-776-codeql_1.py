@app.route("/upload", methods=["POST"])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml = request.data

    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        return "Invalid XML", 400

    return ET.tostring(root), 200