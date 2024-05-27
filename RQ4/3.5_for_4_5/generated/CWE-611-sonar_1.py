from defusedxml import lxml as etree

def get_root():
    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the 'resources/config.xml' file
    tree = etree.parse('resources/config.xml', parser)

    # Return the root element of the XML file
    return tree.getroot()

# Example usage:
# root = get_root()
# print(etree.tostring(root, pretty_print=True).decode())