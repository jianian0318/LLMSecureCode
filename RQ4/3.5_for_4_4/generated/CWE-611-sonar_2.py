import defusedxml.ElementTree as etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return XMLSchema.
    '''
    # Parse the xsd file to get the root element
    tree = etree.parse('resources/config.xsd')
    root = tree.getroot()

    return etree.XMLSchema(root)

# This could be called like:
# try:
#     schema = get_root()
# except Exception as e:
#     print(str(e))