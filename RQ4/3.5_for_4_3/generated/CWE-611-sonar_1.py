import defusedxml.ElementTree as etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    parser = etree.XMLParser(recover=True)
    tree = etree.parse('resources/config.xml', parser)
    return tree.getroot()