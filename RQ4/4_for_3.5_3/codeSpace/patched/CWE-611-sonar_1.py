from lxml import etree

def get_root():
    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the 'resources/config.xml' file
    tree = etree.parse('resources/config.xml', parser)

    # Return the root
    root = tree.getroot()
    return root