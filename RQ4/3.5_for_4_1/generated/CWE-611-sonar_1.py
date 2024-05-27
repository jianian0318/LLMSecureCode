import defusedxml.ElementTree as ET

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # Parse the 'resources/config.xml' file using defusedxml
    tree = ET.parse('resources/config.xml')
    
    # Return the root of the XML tree
    return tree.getroot()