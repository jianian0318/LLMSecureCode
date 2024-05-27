from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    # Parse the 'resources/config.xsd' file using defusedxml
    tree = parse('resources/config.xsd')
    
    # Get the root of the tree
    root = tree.getroot()

    return root