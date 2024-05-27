import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Create an ElementTree object using ET.fromstring() method and pass xml_string to it
    tree = ET.fromstring(xml_string)
    
    # Return the root element of the XML document using getroot() method of the ElementTree object
    return tree.getroot()