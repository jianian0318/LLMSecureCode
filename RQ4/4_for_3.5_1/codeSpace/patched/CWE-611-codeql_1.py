@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.form.get('xml_src')  # get the xml_src from the request form
    parsed_xml = lxml.etree.fromstring(xml_src)  # parse the xml_src using lxml.etree.fromstring()
    return lxml.etree.tostring(parsed_xml)  # return the parsed xml as string using lxml.etree.tostring()