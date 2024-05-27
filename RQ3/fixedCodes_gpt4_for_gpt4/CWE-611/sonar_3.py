from lxml import etree

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    parser = etree.XMLParser(remove_blank_text=True, resolve_entities=False)
    xslt_doc = etree.parse('resources/config.xsl', parser)
    transform = etree.XSLT(xslt_doc)
    return transform