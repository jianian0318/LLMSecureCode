import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Perform proper input validation
    if not isinstance(xml_string, str):
        raise TypeError('xml_string must be a str, not {}'.format(type(xml_string).__name__))
    
    xml_string = escape(xml_string)  # Handling potential harmful characters in xml_string 

    tree = ET.ElementTree(ET.fromstring(xml_string))
    root = tree.getroot()

    return root