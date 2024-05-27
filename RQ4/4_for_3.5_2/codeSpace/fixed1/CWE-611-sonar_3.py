from defusedxml.lxml import parse
from lxml import etree

def transform_xml():
    '''
    Create a XML parser using defusedxml to parse the 'resources/config.xsl' file securely,
    and return an XSLT object.
    '''
    xslt_tree = parse('resources/config.xsl')
    xslt_obj = etree.XSLT(xslt_tree)

    return xslt_obj