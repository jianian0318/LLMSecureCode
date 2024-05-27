import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Use the fromstring() function of the defusedxml.ElementTree module to parse the XML string
    root = ET.fromstring(xml_string)
    
    # Return the root element of the XML document
    return root