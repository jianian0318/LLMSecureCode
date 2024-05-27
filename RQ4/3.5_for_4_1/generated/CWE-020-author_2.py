import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Parse xml_string using defusedxml
    tree = ET.ElementTree(ET.fromstring(xml_string))

    # Get the root element of the XML document
    root = tree.getroot()

    return root