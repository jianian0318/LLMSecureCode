from defusedxml import lxml
from defusedxml.lxml import parse

def transform_xml():
    '''
    Create an XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    parser = lxml.XMLParser(remove_blank_text=True)
    transform = lxml.etree.XSLT(parse('resources/config.xsl', parser=parser))

    return transform