def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Parse the XML string
    root = ET.fromstring(xml_string)
    
    # Return the root element
    return root