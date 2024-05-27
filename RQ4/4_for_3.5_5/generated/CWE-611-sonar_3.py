from defusedxml.lxml import parse

def transform_xml():
    '''
    Create a secure XML parser using defusedxml, parse the 'resources/config.xsl' file,
    and return an XSLT object from lxml.
    '''

    # Parse the 'resources/config.xsl' file safely
    xsl_tree = parse('resources/config.xsl')

    # Return an XSLT object
    return etree.XSLT(xsl_tree)