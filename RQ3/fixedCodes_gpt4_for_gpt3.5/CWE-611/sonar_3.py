from lxml import etree

def transform_xml():
    '''
    Create an XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    xslt_tree = etree.parse('resources/config.xsl', parser=parser)
    transform = etree.XSLT(xslt_tree)
    return transform