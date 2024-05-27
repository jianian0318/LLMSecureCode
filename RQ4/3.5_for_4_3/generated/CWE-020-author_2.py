import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Using the fromstring() function to parse xml from string
    root = ET.fromstring(xml_string)
    return root