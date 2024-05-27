from defusedxml import ElementTree as ET

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # parse 'resources/config.xml' and get the root
    tree = ET.parse('resources/config.xml')
    root = tree.getroot()
    
    return root