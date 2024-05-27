from defusedxml.ElementTree import fromstring as DFfromstring

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    root = DFfromstring(xml_string)
    return root