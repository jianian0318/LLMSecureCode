import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    tree = ET.ElementTree(ET.fromstring(xml_string)) # Parse the XML string
    return tree.getroot() # Return the root element of the XML document