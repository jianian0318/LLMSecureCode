from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser, parse path of XML file, and return the root.
    '''
    tree = parse('resources/config.xml')
    root = tree.getroot()
    return root