import defusedxml.ElementTree as ET
defusedxml.defuse_stdlib()

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    root = ET.fromstring(xml_string)
    return root