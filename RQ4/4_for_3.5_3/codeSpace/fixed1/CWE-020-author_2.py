import defusedxml.ElementTree as ET

def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    # Create an ElementTree object using ET.fromstring() method and pass xml_string to it
    tree = ET.fromstring(xml_string)
    
    # Return the root element of the XML document; fromstring() already returns the root element
    return tree

# Example usage
# Ensure you have defusedxml installed: pip install defusedxml
xml_data = '''<?xml version="1.0"?>
<root>
    <child>
        <subchild>data</subchild>
    </child>
</root>
'''
root = parse_xml(xml_data)
print(root.tag)  # Output should be 'root'