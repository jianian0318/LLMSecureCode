import xml.etree.ElementTree as ET


def parse_xml(xml_string):
    try:
        return ET.fromstring(xml_string)
    except ET.ParseError:
        return None