from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''

    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the 'resources/config.xml' file and get the root element
    tree = etree.parse('resources/config.xml', parser=parser)
    root = tree.getroot()

    # Return the root element
    return root