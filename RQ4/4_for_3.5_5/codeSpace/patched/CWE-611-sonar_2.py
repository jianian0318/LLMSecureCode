def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    # Create an XML parser
    parser = etree.XMLParser()

    # Parse the 'resources/config.xsd' file
    xml_file = etree.parse('resources/config.xsd', parser)

    # Return the root of the parsed XML file
    return xml_file.getroot()