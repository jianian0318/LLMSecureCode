from defusedxml.lxml import parse, fromstring
from lxml.etree import XSLT

def transform_xml():
    '''
    Create a XML parser using defusedxml to parse the 'resources/config.xsl' file securely,
    and return an XSLT object.
    '''
    xslt_tree = parse('resources/config.xsl')
    xslt_obj = XSLT(xslt_tree)

    return xslt_obj