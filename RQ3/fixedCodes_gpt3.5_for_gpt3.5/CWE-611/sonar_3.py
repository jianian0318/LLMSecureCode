from lxml import etree


def transform_xml():
    '''
    Create an XML parser, disable external entity references,
    parse the 'resources/config.xsl' file, and return an XSLT object.
    '''
    parser = etree.XMLParser(load_dtd=False, no_network=True)
    xslt_tree = etree.parse('resources/config.xsl', parser=parser)
    transform = etree.XSLT(xslt_tree)
    return transform