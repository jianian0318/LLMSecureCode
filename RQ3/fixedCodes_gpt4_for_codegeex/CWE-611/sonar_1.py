from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Create an XML parser
    parser = etree.XMLParser(encoding='utf-8', resolve_entities=False)
    # Parse the 'resources/config.xml' file
    root = etree.parse('resources/config.xml', parser)
    # Return the root element
    return root.getroot()