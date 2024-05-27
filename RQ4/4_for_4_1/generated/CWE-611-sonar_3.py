from defusedxml.lxml import parse

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Parse the 'resources/config.xsl' file
    xsl_doc = parse('resources/config.xsl')

    # Create an XSLT object
    transform = etree.XSLT(xsl_doc)

    return transform