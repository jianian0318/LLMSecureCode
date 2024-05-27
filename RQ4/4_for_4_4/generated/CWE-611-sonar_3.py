from defusedxml.lxml import parse

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # parse the xsl file
    xsl_root = parse('resources/config.xsl')
    
    # create an XSLT transform
    transform = etree.XSLT(xsl_root)
    
    return transform