import defusedxml.ElementTree as etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    # Create XML parser
    parser = etree.XMLParser()

    # Parse the XML file
    xml_tree = etree.parse('resources/config.xsd', parser)

    # Return the XML Schema
    return etree.XMLSchema(xml_tree)