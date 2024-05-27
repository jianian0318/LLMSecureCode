from defusedxml import lxml

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Create an XML parser object
    parser = lxml.XMLParser()
    
    # Parse the 'resources/config.xml' file and get the root element
    tree = lxml.parse('resources/config.xml', parser)
    root = tree.getroot()
    
    return root