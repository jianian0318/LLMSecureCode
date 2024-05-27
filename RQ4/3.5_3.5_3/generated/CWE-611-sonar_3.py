import defusedxml.ElementTree as etree

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    xml_parser = etree.XMLParser()
    with open('resources/config.xsl', 'rb') as f:
        xslt_doc = etree.parse(f, xml_parser)
    xslt = etree.XSLT(xslt_doc)
    return xslt