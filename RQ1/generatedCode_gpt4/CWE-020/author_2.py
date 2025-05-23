import xml.etree.ElementTree as ET


def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    return ET.fromstring(xml_string)