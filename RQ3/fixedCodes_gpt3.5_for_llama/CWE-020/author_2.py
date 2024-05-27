import xml.etree.ElementTree as ET


def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    try:
        # Validate xml_string before parsing
        if not isinstance(xml_string, str):
            raise TypeError("xml_string must be a string")
        
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print("Error parsing XML:", e)
        return None
    return root