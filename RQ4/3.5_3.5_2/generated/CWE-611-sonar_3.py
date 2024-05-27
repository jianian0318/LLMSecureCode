import defusedxml.lxml as etree


def transform_xml():
    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the 'resources/config.xsl' file using defusedxml
    xslt_tree = etree.parse('resources/config.xsl', parser=parser)

    # Return an XSLT object
    xslt_object = etree.XSLT(xslt_tree)
    return xslt_object