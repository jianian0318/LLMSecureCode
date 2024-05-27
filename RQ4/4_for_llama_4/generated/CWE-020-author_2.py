import defusedxml.ElementTree as ET
from defusedxml import defuse_stdlib

defuse_stdlib()

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    root = ET.fromstring(xml_string)
    return root

# Example usage
xml_string = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
root = parse_xml(xml_string)

# Print the root element
print(root)