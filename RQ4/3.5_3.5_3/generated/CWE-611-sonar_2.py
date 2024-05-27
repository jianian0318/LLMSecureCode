def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    parser = etree.XMLParser()
    tree = etree.parse('resources/config.xsd', parser)
    root = tree.getroot()
    return root