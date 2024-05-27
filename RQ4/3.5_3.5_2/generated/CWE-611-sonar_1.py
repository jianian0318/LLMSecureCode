from defusedxml import ElementTree as etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Parse the 'resources/config.xml' file using defusedxml
    tree = etree.parse('resources/config.xml')

    # Get the root of the XML tree
    root = tree.getroot()

    return root