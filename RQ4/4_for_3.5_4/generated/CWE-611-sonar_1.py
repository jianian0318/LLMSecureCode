from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file using defusedxml, and return the root.
    '''
    tree = parse('resources/config.xml')
    root = tree.getroot()
    return root