import defusedxml.lxml

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''

    # Create an XML parser
    parser = defusedxml.lxml.XMLParser()

    # Parse the 'resources/config.xsl' file
    xsl_tree = defusedxml.lxml.parse('resources/config.xsl', parser)

    # Return an XSLT object
    transform = defusedxml.lxml.XSLT(xsl_tree)

    return transform