from lxml import etree


def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return the root element.
    '''
    parser = etree.XMLParser(no_network=True)
    tree = etree.parse('resources/config.xsd', parser)
    root = tree.getroot()
    
    return root