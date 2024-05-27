import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # parse the XML string using ElementTree safely with defusedxml
    tree = ET.ElementTree(ET.fromstring(xml_string))
    
    # get the root element of the XML document
    root = tree.getroot()
    
    # return the root element
    return root