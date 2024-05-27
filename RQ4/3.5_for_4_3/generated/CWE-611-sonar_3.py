from defusedxml import etree

def transform_xml():
    """
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    """
    parser = etree.XMLParser()  # Create an XML parser
    xslt_root = etree.parse('resources/config.xsl', parser=parser)  # Parse the XSL file
    xslt = etree.XSLT(xslt_root)  # Create an XSLT object
    return xslt

# Example usage
# assuming that there is a file resources/config.xsl available in your directory
xslt_transformer = transform_xml()
# Now you can use xslt_transformer to apply the transformation to some XML data