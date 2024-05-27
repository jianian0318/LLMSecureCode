from lxml import etree


def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    parser = etree.XMLParser(recover=True, no_network=True)
    xslt_tree = etree.parse('resources/config.xsl', parser)
    xslt = etree.XSLT(xslt_tree)
    return xslt