def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the 'resources/config.xml' file and return the root
    tree = etree.parse('resources/config.xml', parser)
    root = tree.getroot()

    return root