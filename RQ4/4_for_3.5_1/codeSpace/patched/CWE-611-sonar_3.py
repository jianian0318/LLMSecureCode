from lxml import etree

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Create an XML parser
    parser = etree.XMLParser()
    
    # Parse the 'resources/config.xsl' file
    xslt_tree = etree.parse('resources/config.xsl', parser)
    
    # Return an XSLT object
    return etree.XSLT(xslt_tree)