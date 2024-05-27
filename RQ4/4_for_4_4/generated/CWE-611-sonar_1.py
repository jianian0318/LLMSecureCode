from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Parse xml file and get the root
    root = parse('resources/config.xml').getroot()

    return root