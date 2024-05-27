@app.route("/upload", methods=["POST"])
def upload():
    xml_src = request.data.decode("utf-8")

    # Parse the XML
    try:
        xml_root = lxml.etree.fromstring(xml_src)
    except lxml.etree.XMLSyntaxError:
        return "Invalid XML", 400

    # Convert XML root to string
    xml_str = lxml.etree.tostring(xml_root, pretty_print=True).decode("utf-8")

    # Return the parsed XML as a string
    return xml_str