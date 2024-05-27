from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    tree = parse('resources/config.xsd')
    return tree.getroot()