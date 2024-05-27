from defusedxml import ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # use ET.fromstring function to parse XML document from a string
    root = ET.fromstring(xml_string)
    return root