import xml.etree.ElementTree as ET

def get_root():
    '''
    Parse the 'resources/config.xml' file and return the root element.
    '''
    # Parse the 'resources/config.xml' file
    tree = ET.parse('resources/config.xml')
    # Get the root element
    root = tree.getroot()
    # Return the root element
    return root