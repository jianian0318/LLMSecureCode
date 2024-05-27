import xml.etree.ElementTree as ET
import xml.sax.saxutils as saxutils

def parse_xml(xml_string):
    '''
    Parse xml_string and validate that it is well-formed XML.
    Then return the root element of the XML document.
    '''
    xml_string = saxutils.escape(xml_string)
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError:
        print('Invalid or malicious XML detected: ParseError')
        return None
        
    return root