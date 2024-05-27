from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return the root element of the XML document.
    '''
    parser = etree.XMLParser(recover=True)
    tree = etree.parse('resources/config.xsd', parser)
    root = tree.getroot()
    return root