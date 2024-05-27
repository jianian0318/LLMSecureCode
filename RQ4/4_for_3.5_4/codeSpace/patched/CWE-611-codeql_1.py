@app.route("/upload", methods=["POST"])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    # Get the xml_src from the request
    xml_src = request.data

    # Parse the XML
    root = lxml.etree.fromstring(xml_src)

    # Convert the parsed XML to string
    parsed_xml = lxml.etree.tostring(root, encoding=str)

    # Return the parsed XML as string
    return parsed_xml