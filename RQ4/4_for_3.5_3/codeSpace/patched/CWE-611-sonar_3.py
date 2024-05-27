from lxml import etree

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the XML file 'resources/config.xsl' and return an etree.ElementTree object
    tree = etree.parse('resources/config.xsl', parser)

    # Create an XSLT object from the parsed XML tree
    xslt = etree.XSLT(tree)

    return xslt