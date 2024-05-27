import os
from lxml import etree

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    parser = etree.XMLParser(remove_blank_text=True)
    xslt_path = os.path.join(os.getcwd(), 'resources', 'config.xsl')
    xslt_tree = etree.parse(xslt_path, parser)
    transform = etree.XSLT(xslt_tree)
    return transform