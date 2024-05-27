from defusedxml.ElementTree import parse

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Safe parsing of the XML string
    root = parse(xml_string).getroot()
    return root