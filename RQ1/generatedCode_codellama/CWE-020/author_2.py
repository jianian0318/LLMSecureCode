import xml.etree.ElementTree as ET


def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print("Error parsing XML:", e)
        return None
    return root
