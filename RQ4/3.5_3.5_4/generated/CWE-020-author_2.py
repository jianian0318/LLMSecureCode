def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Parse xml_string using ElementTree's fromstring method
    root = ET.fromstring(xml_string)
    
    # Return the root element
    return root