from defusedxml.lxml import parse


def transform_xml():
    '''
    Create an XML parser using defusedxml, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Parse with defusedxml to mitigate XML attacks
    xslt_tree = parse('resources/config.xsl')
    xslt = etree.XSLT(xslt_tree)
    return xslt