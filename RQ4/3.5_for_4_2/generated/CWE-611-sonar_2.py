from defusedxml import lxml as etree


def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    # Create an defusedxml.lxml.etree.XMLParser object
    parser = etree.XMLParser()
    # Parse the XML file
    tree = etree.parse('resources/config.xsd', parser)
    # Get the root element of the XML document
    root = tree.getroot()
    # Return the XMLSchema
    return etree.XMLSchema(root)