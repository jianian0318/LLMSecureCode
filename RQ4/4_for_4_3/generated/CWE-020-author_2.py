# Make sure you have installed the defusedxml library
# You can install it using: pip install defusedxml

import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Parse the xml string using defusedxml to prevent XML attacks
    tree = ET.fromstring(xml_string)
    
    # Get and return the root element of the xml document
    return tree

# Example usage:
# xml_data = '<your_xml_string_here>'
# parsed_tree = parse_xml(xml_data)