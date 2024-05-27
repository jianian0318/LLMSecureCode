from defusedxml.lxml import parse

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Parse the 'resources/config.xsl' file
    xslt_tree = parse('resources/config.xsl')
    
    # Return an XSLT object
    return etree.XSLT(xslt_tree)