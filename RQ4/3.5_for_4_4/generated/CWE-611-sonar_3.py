import defusedxml.lxml as etree


def transform_xml():
    # Create a parser
    parser = etree.XMLParser()

    # Parse the 'resources/config.xsl' file
    root = etree.parse('resources/config.xsl', parser)

    # Create XSLT object
    xslt = etree.XSLT(root)

    # Return XSLT object
    return xslt