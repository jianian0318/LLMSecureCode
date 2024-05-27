def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    xml_parser = etree.XMLParser()
    xml_schema = etree.XMLSchema(file='resources/config.xsd', parser=xml_parser)
    
    return xml_schema