import defusedxml.ElementTree as ET

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    # Get the xml_src from the request
    xml_src = request.form.get('xml_src')

    # Parse the XML
    root = ET.fromstring(xml_src)

    # Convert the parsed XML back to string
    xml_str = ET.tostring(root, encoding='unicode')

    return xml_str