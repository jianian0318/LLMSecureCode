import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Parse the XML string and get the root element
    ET.defuse_stdlib()
    root = ET.fromstring(xml_string)
    return root