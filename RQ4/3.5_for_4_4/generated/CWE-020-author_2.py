import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Ensure defusedxml is used to parse the XML data
    defusedxml.defuse_stdlib()
    
    # Data is passed as a string to the XML parser
    root = ET.fromstring(xml_string)
    return root