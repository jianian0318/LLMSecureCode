from defusedxml.lxml import parse

def transform_xml():
    '''
    Safely create an XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object using defusedxml to prevent XML vulnerabilities.
    '''
    # Safely parse the XML file 'resources/config.xsl' and return an etree.ElementTree object
    tree = parse('resources/config.xsl')

    # Create an XSLT object from the parsed XML tree
    xslt = tree.xslt()

    return xslt