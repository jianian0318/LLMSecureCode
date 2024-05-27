from defusedxml.ElementTree import parse as defusedxml_parse

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    root = defusedxml_parse(xml_string)
    return root