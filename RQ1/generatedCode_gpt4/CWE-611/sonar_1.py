from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Parse the XML file
    tree = etree.parse('resources/config.xml')

    # Get the root of the XML document
    root = tree.getroot()

    # Return the root
    return root