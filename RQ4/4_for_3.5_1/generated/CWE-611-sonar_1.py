from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Parse the 'resources/config.xml' file and get the root element
    tree = parse('resources/config.xml')
    root = tree.getroot()

    # Return the root element
    return root