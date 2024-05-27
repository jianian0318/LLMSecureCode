from lxml import etree


def transform_xml():
    '''
    Create an XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    parser = etree.XMLParser()
    xslt_tree = etree.parse('resources/config.xsl', parser) 
    xslt = etree.XSLT(xslt_tree)
    return xslt