import xml.etree.ElementTree as ET
import defusedxml.ElementTree as DefusedET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    try:
        parser = DefusedET.defuse_stdlib()
        root = ET.fromstring(xml_string, parser=parser)
    except ET.ParseError as e:
        print("Error parsing XML:", e)
        return None
    return root