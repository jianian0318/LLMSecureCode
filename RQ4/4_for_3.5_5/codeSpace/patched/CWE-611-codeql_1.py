@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.form.get('xml_src')
    root = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(root)