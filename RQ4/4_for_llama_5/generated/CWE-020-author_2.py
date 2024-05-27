from defusedxml.ElementTree import parse, fromstring

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    root = fromstring(xml_string)
    return root

xml_string = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
root = parse_xml(xml_string)
print(root)