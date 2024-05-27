from defusedxml import etree

def get_root():
    # Create an XML parser
    parser = etree.DefusedXMLParser()

    # Parse the 'resources/config.xml' file
    tree = etree.parse('resources/config.xml', parser)

    # Return the root of the XML tree
    return tree.getroot()

# Example usage
root = get_root()