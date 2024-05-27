from defusedxml.lxml import parse

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    tree = parse('resources/config.xsl')
    return etree.XSLT(tree)