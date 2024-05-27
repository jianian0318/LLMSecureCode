from defusedxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    # Define XML parser
    parser = etree.XMLParser()

    # Parse 'resources/config.xsd' file
    tree = etree.parse('resources/config.xsd', parser)

    # Get the root of the XMLSchema
    root = tree.getroot()

    return root