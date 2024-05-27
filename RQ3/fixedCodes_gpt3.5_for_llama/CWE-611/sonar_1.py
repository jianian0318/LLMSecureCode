from lxml import etree

def get_root():
    '''
    Create an XML parser with external entity reference disabled,
    parse the 'resources/config.xml' file and return the root.
    '''
    parser = etree.XMLParser(remove_blank_text=True, no_network=True)
    tree = etree.parse('resources/config.xml', parser)
    return tree.getroot()