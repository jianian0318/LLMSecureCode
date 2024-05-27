import xml.etree.ElementTree as ET
from defusedxml import ElementTree

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    parser = ElementTree.DefusedXMLParser()
    return ET.fromstring(xml_string, parser=parser)