from defusedxml import lxml

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.data
    root = lxml.fromstring(xml_src)
    return lxml.tostring(root).decode()