def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the XML file
    xslt_tree = etree.parse('resources/config.xsl', parser)

    # Return the XSLT object
    return etree.XSLT(xslt_tree)