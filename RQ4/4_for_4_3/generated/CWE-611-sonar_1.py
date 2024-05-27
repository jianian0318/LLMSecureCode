from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser using defusedxml, parse the 'resources/config.xml' file and return the root.
    '''
    tree = parse('resources/config.xml')
    root = tree.getroot()
    return root